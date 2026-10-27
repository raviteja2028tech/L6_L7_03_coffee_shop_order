
import pytest

from coffee_shop_order import (
    process_order_batch,
    check_espresso_machine,
)


def make_order(**overrides):
    order = {
        "paid": True,
        "size": "medium",
        "strict_allergy": False,
        "is_member": False,
        "customizations": [],
    }
    order.update(overrides)
    return order


# 1. Input validation
def test_invalid_orders_input():
    with pytest.raises(ValueError):
        process_order_batch("invalid", 0.1)


def test_negative_tax_rate():
    with pytest.raises(ValueError):
        process_order_batch([], -0.1)


# 2. Payment and coffee sizes
def test_unpaid_order():
    result = process_order_batch([make_order(paid=False)], 0.1)
    assert result["status"] == "NO_SALE"


def test_small_coffee():
    result = process_order_batch([make_order(size="small")], 0)
    assert result["total"] == 3.0


def test_medium_coffee():
    result = process_order_batch([make_order(size="medium")], 0)
    assert result["total"] == 4.5


def test_large_coffee():
    result = process_order_batch([make_order(size="large")], 0)
    assert result["total"] == 6.0


def test_invalid_coffee_size():
    result = process_order_batch([make_order(size="extra-large")], 0)
    assert result["status"] == "NO_SALE"


# 3. Customizations
def test_negative_customization_cost():
    result = process_order_batch(
        [make_order(customizations=[
            {"type": "standard", "cost": -1}
        ])],
        0,
    )
    assert result["status"] == "COMPLETED"
    assert result["total"] == 4.5


def test_syrup_cost_at_boundary():
    result = process_order_batch(
        [make_order(customizations=[
            {"type": "syrup", "cost": 1.5}
        ])],
        0,
    )
    assert result["total"] == 6.0


def test_syrup_cost_above_boundary():
    result = process_order_batch(
        [make_order(customizations=[
            {"type": "syrup", "cost": 2.0}
        ])],
        0,
    )
    assert result["total"] == 6.0


def test_standard_customization():
    result = process_order_batch(
        [make_order(customizations=[
            {"type": "standard", "cost": 0.5}
        ])],
        0,
    )
    assert result["total"] == 5.0


# 4. Membership and allergy handling
def test_member_discount():
    result = process_order_batch(
        [make_order(is_member=True)],
        0,
    )
    assert result["total"] == 4.05


def test_strict_allergy():
    result = process_order_batch(
        [make_order(
            strict_allergy=True,
            customizations=[
                {"type": "allergen_alert", "cost": 0}
            ],
        )],
        0,
    )
    assert result["total"] == 0


def test_non_strict_allergy():
    result = process_order_batch(
        [make_order(
            customizations=[
                {"type": "allergen_alert", "cost": 0.5}
            ]
        )],
        0,
    )
    assert result["total"] == 4.5
    assert result["status"] == "COMPLETED"


# 5. Rejected orders and tax
def test_audit_rejected():
    orders = [make_order(size="unknown") for _ in range(5)]
    result = process_order_batch(orders, 0)
    assert result["status"] == "AUDIT_REJECTED"


def test_tax_calculation():
    result = process_order_batch([make_order()], 0.1)
    assert result["total"] == 4.95


# 6. Espresso machine monitoring
def test_empty_temperature_data():
    assert check_espresso_machine([]) == "NO_DATA"


def test_machine_shutdown():
    assert check_espresso_machine([[97, 97]]) == "SHUTDOWN"


def test_temperature_recovery():
    assert check_espresso_machine([[97, 95, 97]]) == "OPTIMAL"


def test_separate_temperature_cycles():
    assert check_espresso_machine([[97], [97]]) == "OPTIMAL"
