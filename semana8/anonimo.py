def hacer_suma():
   resul = 2+5
   return resul
#variable = lambda args : exp
#variable()

#lambda es pal anonimato

resul = lambda: 2+5
print(resul())

variable = lambda : "lo que se ejecuta"

info = variable()
print (info)

resul = lambda : 5+2
info = resul()
print(f"resultado es: {info}")

