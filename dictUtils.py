# =============================================================================
# PARENT MODULES

if __name__ == "__main__":
   import nicePrints as np
else:
   from . import nicePrints as np

# =============================================================================

# style = 1 
# chiave
#        valore
# chiave
#        valore
# ...
#        ...
#
#style = 2 
# chiave       valore
# chiave       valore
# chiave       valore
def fancyPrint(inputDictionary: dict, indent=0, style=1):
   if(style != 1 and style != 2):
      np.errorPrint("dictUtils.fancyPrint(): Stile non valido. Imposto per default stile 1")
      style = 1

   for key, value in inputDictionary.items():

      if(style == 1):
         print(('\t' * indent) + str(key))
      
      if(style == 2):
         print(('\t' * indent) + str(key),end='')
      
      if isinstance(value, dict):
         fancyPrint(value, indent+1)
      else:
         print('\t' * (indent+1) + str(value))