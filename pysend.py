import serial

UART2_PORT = "/dev/ttyO2"
UART1_PORT = "/dev/ttyO1"
UART_BAUD = 9600
UART2_TX = "spi0_d0"
UART2_RX = "spi0_sclk"
UART2_MUX = 1
UART1_TX = "uart1_txd"
UART1_RX = "uart1_rxd"
UART1_MUX = 0

open("/sys/kernel/debug/omap_mux/" + UART1_TX, "wb").write("%x" % UART1_MUX)
v = open("/home/ubuntu/Code/cam1.txt", 'r').read()
v = v[:1]
print v
ulcd = serial.Serial(UART1_PORT, UART_BAUD)
ulcd.write(v)
	
