
from tools import *

def main():
    # Test connection and basic operations
    print("Testing MongoDB Connection and Basic Operations...")

    # Test Post Transaction
    transaction_data = {
        "saleDate": "2023-10-01T14:20:00Z",
        "items": [
            {"name": "notebook", "tags": ["office", "writing"], "price": 9.99, "quantity": 10},
            {"name": "pen", "tags": ["office", "writing"], "price": 1.99, "quantity": 100}
        ],
        "storeLocation": "New York",
        "customer": {"gender": "M", "age": 30, "email": "test@example.com", "satisfaction": 5},
        "couponUsed": False,
        "purchaseMethod": "Online"
    }
    transaction_id = post_transaction(transaction_data)
    print("Inserted Transaction ID:", transaction_id)

    # Test Get Transactions
    transactions = get_transactions({"storeLocation": "New York"})
    print("Transactions:", transactions)

    # Test Update Transaction
    update_result = update_transaction(transaction_id, {"couponUsed": True})
    print("Updated Count:", update_result)

    # Test Delete Transaction
    delete_result = delete_transaction(transaction_id)
    print("Deleted Count:", delete_result)

    # Analytics and Reporting Tests
    print("Testing Analytics and Reporting...")
    summary = sales_summary()
    print("Sales Summary:", summary)

    revenue = revenue_analysis()
    print("Revenue Analysis:", revenue)

    # Customer Management Tests
    print("Testing Customer Management...")
    customers = get_customers({"customer.email": "test@example.com"})
    print("Customers:", customers)

    update_customer = update_customer_info("test@example.com", {"age": 31})
    print("Updated Customer Info Count:", update_customer)

    purchase_history = customer_purchase_history("test@example.com")
    print("Purchase History:", purchase_history)

    # Item Management Tests
    print("Testing Item Management...")
    items = get_items()
    print("Items:", items)

    update_items = update_item("notebook", {"price": 11.99})
    print("Updated Items Count:", update_items)

    # Store Management Tests
    print("Testing Store Management...")
    stores = list_stores()
    print("List of Stores:", stores)

    performance = store_performance()
    print("Store Performance:", performance)

if __name__ == "__main__":
    main()