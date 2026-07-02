import random
from sqlalchemy.orm import Session
from src.core.database import SessionLocal
from src.models.vendor import Vendor
from src.models.vendor_quote import VendorQuote
from src.models.procurement_request import ProcurementRequest 


def seed_data():
    # Use context manager to handle automatic session closing and cleanup
    with SessionLocal() as db:
        try:
            # -----------------------------
            # CLEAR OLD DATA
            # -----------------------------
            # Delete child tables first to avoid foreign key constraint issues
            db.query(VendorQuote).delete()
            db.query(Vendor).delete()
            db.query(ProcurementRequest).delete() 
            db.commit()

            # -----------------------------
            # VENDORS
            # -----------------------------
            vendors = [
                Vendor(id=1, name="TechSupply Ltd", rating=4.7),
                Vendor(id=2, name="Global Procurement Co", rating=4.1),
                Vendor(id=3, name="QuickSource Traders", rating=3.6),
                Vendor(id=4, name="BudgetMart Supplies", rating=3.2),
                Vendor(id=5, name="Elite Industrial Co", rating=4.8),
                Vendor(id=6, name="East Africa Supplies", rating=3.9),
            ]
            db.add_all(vendors)
            db.commit()

            # -----------------------------
            # CREATE PROCUREMENT REQUESTS
            # -----------------------------
            # Added required 'title' and 'description' strings to fix the IntegrityError
            req_objects = [
                ProcurementRequest(
                    id=1, 
                    title="MacBook Pro Procurement", 
                    description="10x Developer Laptops",
                    quantity=10,
                    status="pending"
                ),  
                ProcurementRequest(
                    id=2, 
                    title="Ergonomic Office Chairs", 
                    description="25x Mesh back chairs for Floor 3",
                    quantity=25,
                    status="pending"
                ),
                ProcurementRequest(
                    id=3, 
                    title="Server Room Air Conditioner", 
                    description="Heavy-duty cooling unit replacement",
                    quantity=1,
                    status="pending"
                )
            ]
            db.add_all(req_objects)
            db.commit()

            # -----------------------------
            # QUOTES GENERATION
            # -----------------------------
            quotes = []
            quote_id = 1
            request_ids = [1, 2, 3]

            for req_id in request_ids:
                for v in vendors:
                    price = random.randint(500, 1200)
                    delivery = random.randint(3, 20)

                    quote = VendorQuote(
                        id=quote_id,
                        request_id=req_id,
                        vendor_id=v.id,
                        price=price,
                        delivery_days=delivery
                    )
                    quotes.append(quote)
                    quote_id += 1

            db.add_all(quotes)
            db.commit()

            print("Dummy procurement data seeded successfully!")
            
        except Exception as e:
            db.rollback()
            print(f" Seeding failed, transaction rolled back. Error: {e}")
            raise e


if __name__ == "__main__":
    seed_data()