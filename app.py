from scriptPDF import createPDF

if __name__ == '__main__':    
    createPDF(Y=32, X=28, Font='Arial', Size=12, target_page=1, Text=["Hospital 1", "123 Anytown land, suite 123", "Phoenix, AZ 92929"])