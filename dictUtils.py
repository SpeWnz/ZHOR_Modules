# =============================================================================
# PARENT MODULES

if __name__ == "__main__":
    pass
else:
    pass

# =============================================================================

def fancyPrint(inputDictionary: dict, indent=0):
   for key, value in inputDictionary.items():
      print('\t' * indent + str(key))
      if isinstance(value, dict):
         pretty(value, indent+1)
      else:
         print('\t' * (indent+1) + str(value))