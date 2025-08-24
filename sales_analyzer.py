# import csv

# with open('sales_data.csv', 'r') as file:
#     reader = csv.reader(file)
#     header= next(reader)

#     for row in reader:
#         print(row)

import csv

class SalesAnalyzer:
    def __init__(self,file_name = "sales_data.csv"):
        self.filename = file_name

    def load_data(self,product_name,price,quantity,date,region):
        with open('sales_data.csv', 'r') as file:
            reader = csv.reader(file)
            header = next(reader)

            for row in reader:
                if not row:
                    continue
                if row[0].lower() == product_name.lower():
                    print("............product already exists in store.........")
                    return
        with open('sales_data.csv','a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([product_name , price , quantity , date , region])
            print("............New product added successfully.........")

    def revenue(self):
        total_revenue =0
        with open('sales_data.csv','r') as file:
            reader =csv.DictReader(file)
            for row in reader:
                    price = float(row["Price"])
                    quantity = float(row["Quantity"])
                    revenue = price * quantity 
                    total_revenue += revenue
                    print(f"{row["Product Name"]} {row["Region"]}=> Revenue:{revenue}")
        print(f"Total revenue of the sales is:  {total_revenue}")
        

    def top_products(self):
        top_product = {}

        with open('sales_data.csv','r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                price = float(row["Price"])
                quantity = float(row["Quantity"])
                revenue = price * quantity
                product = row['Product Name']
                top_product[product] = top_product.get(product, 0) + revenue

        top = sorted(top_product.items(), key=lambda x: x[1], reverse=True)[:3]
        print("The top 3 products with most sales are:\n")
        max_revenue = top[0][1] if top else 1
        for product, revenue in top:
            bar_length = int((revenue / max_revenue) * 50)
            print(f"{product:<12} | {'█' * bar_length} {revenue:,.0f}")

    def regional_performance(self):
        region_sales = {}

        with open(self.filename, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                price = float(row["Price"])
                quantity = float(row["Quantity"])
                revenue = price * quantity
                region = row["Region"]

                region_sales[region] = region_sales.get(region, 0) + revenue

        print("\nRegional Performance:")
        for region, revenue in region_sales.items():
            print(f"{region}: {revenue:,.0f}")



analyzer =SalesAnalyzer()
# # analyzer.load_data("Buds",800,1,"2025-08-16","north")
# analyzer.revenue()
# analyzer.top_products()
analyzer.regional_performance()

# with open('sales_data.csv', 'r') as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(row['Product Name'], row['Price'], row['Quantity'], row['Region'])