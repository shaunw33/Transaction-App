# Transaction App (Shaun Wilkerson)

For the online shopping application, users will be able to add 
clothing items to their shopping cart


## To run the program

Click Run green triangle icon in the top right corner
of the Pycharm window
```shell
Project_GUI_aswilke1 .py
```

## Functionality
### Add an item to cart

A new item will be added to the cart at the press of any button    
titled 'Add to Cart'

### Check Out

Once customers are ready to check out their order, they simply 
just click the Check Out button which finalizes their order

### Exit

The application will exit when the Exit button is clicked.\

## Data files

### transactions.csv

This contains the transaction data in the following format

| Item Name | Item Price | Time     | Stock      | 
|-----------|------------|----------|------------|
| Jacket    | $79.99     | Wed Nov  | 1 Quantity |

### customers.json
This contains the information related to the bank customers 
in the following format:

```json
Layered Active Jacket,79.99,Wed Nov 30 21:06:12 2022, 1 Quantity
Knit Cuffed Beanie,9.99,Wed Nov 30 21:06:13 2022,1 Quantity
```

### Class

#### Variables
The class has one Class variable: Item

Each Accounts instance/object has 3 instance variables:
1. name: string data type
2. price: float
3. stock: string

#### Methods
The Item class has the following methods:
* The dunder "__init__" method


## Auto Testing
Run the following command to test the file. Enter the following command in the Terminal:

```shell
$ pip install pytest
$ pytest -v
```



