#Current from High fidility sensor 

def decimal_to_binary(input_number):
  return list(str("{0:0b}".format(input_number).zfill(12)))

def current_from_sensor(current_bit):
  current_bit=''.join(current_bit)
  current_dec= int(current_bit, 2)
  if 0< current_dec < 4095:
    current_amp= round(10*current_dec/4094)
    return current_amp
  
