order = [
    {
        "idpizza":1,
        "ingredientes":[{"idingr":1, "cantidad":20},{"idingr":2, "cantidad":40},{"idingr":3, "cantidad":20},{"idingr":4, "cantidad":12}]
    },
    {    
        "idpizza":2,
        "ingredientes":[{"idingr":1, "cantidad":30},{"idingr":2, "cantidad":3},{"idingr":3, "cantidad":5},{"idingr":4, "cantidad":5}]
    },
 {    
         "idpizza":3,
        "ingredientes":[{"idingr":1, "cantidad":10},{"idingr":2, "cantidad":5},{"idingr":3, "cantidad":8},{"idingr":4, "cantidad":4}]
    },
     {    
         "idpizza":4,
        "ingredientes":[{"idingr":1, "cantidad":5},{"idingr":2, "cantidad":5},{"idingr":3, "cantidad":16},{"idingr":4, "cantidad":16}]
    },
]
supliertotalingredientes = {}
for pizza in order:
    ingredientes = pizza["ingredientes"]
    for valoresingrediente in ingredientes:
         if (supliertotalingredientes.get(valoresingrediente["idingr"]) == None):
            supliertotalingredientes[valoresingrediente["idingr"]] = valoresingrediente["cantidad"]
         else:
            supliertotalingredientes[valoresingrediente["idingr"]] += valoresingrediente["cantidad"]

print(supliertotalingredientes)