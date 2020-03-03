# MFC_Control
Control Standard Mass Flow Controllers using 2 arduinos

COM ports used for arduinos need to beedited in the MFC_gui_final.py file 
  read_ser is for arduino reading in flow data using the Read_MFC_Data arduino code 
  send_ser is for the arduino providing setpoints using Multichannel_Flow_meter_arduino)

Only outside python package required is pyserial, all other libraries should come standard with python instillations
