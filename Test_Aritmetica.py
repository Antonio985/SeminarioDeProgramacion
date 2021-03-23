#importacion oara poder trabajar con las funciones
#from Modulos import Modulo_Aritmetica as aritmetica
import Modulos.Modulo_Aritmetica as aritmetica

#utilizaremos las funciones
resultado = aritmetica.sumar(10,5)
resultador = aritmetica.restar(10,5)
resultadom = aritmetica.multiplicar(10,5)
resultadod = aritmetica.dividir(10,5)

#Enviamos a impresion
print("El Resultado de la suma es : ",resultado)
print("El Resultado de la resta es : ",resultador)
print("El Resultado de la multiplicacion es : ",resultadom)
print("El Resultado de la division es : ",resultadod)

