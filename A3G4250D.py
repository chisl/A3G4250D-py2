#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""A3G4250D: MEMS motion sensor: 3-axis digital output gyroscope"""

__author__     = "ChISL"
__copyright__  = "TBD"
__credits__    = ["STMicroelectronics"]
__license__    = "TBD"
__version__    = "Version 0.1"
__maintainer__ = "https://chisl.io"
__email__      = "info@chisl.io"
__status__     = "Test"

#
#   THIS FILE IS AUTOMATICALLY CREATED
#    D O     N O T     M O D I F Y  !
#

from A3G4250D_constants import *

# name:        A3G4250D
# description: MEMS motion sensor: 3-axis digital output gyroscope
# manuf:       STMicroelectronics
# version:     Version 0.1
# url:         http://www.st.com/resource/en/datasheet/a3g4250d.pdf
# date:        2018-01-23


# Derive from this class and implement read and write
class A3G4250D_Base:
	"""MEMS motion sensor: 3-axis digital output gyroscope"""
	# Register WHO_AM_I
	# 7.1
	#       Device identification register. 
	
	
	def setWHO_AM_I(self, val):
		"""Set register WHO_AM_I"""
		self.write(REG.WHO_AM_I, val, 8)
	
	def getWHO_AM_I(self):
		"""Get register WHO_AM_I"""
		return self.read(REG.WHO_AM_I, 8)
	
	# Bits WHO_AM_I
	# Register CTRL_REG1
	# 7.2 
	#       In the following table (Table 22) all frequencies resulting in a combination of 
	#       DR / BW bits are reported. ODR in Hz.
	#       DR  BW  ODR  Cut-off
	#       00  00  100  12.5
	#       00  01  100  25
	#       00  10  100  25
	#       00  11  100  25
	#       01  00  200  12.5
	#       01  01  200  25
	#       01  10  200  50
	#       01  11  200  70
	#       10  00  400  20
	#       10  01  400  25
	#       10  10  400  50
	#       10  11  400  110
	#       11  00  800  30
	#       11  01  800  35
	#       11  10  800  50
	#       11  11  800  110 
	# Combination of PD, Zen, Yen, and Xen are used to set the device in different modes
	#       (power-down / normal / sleep mode) according to the following table.
	#       Table 23.     Power mode selection configuration
	#       Mode	      PD Zen Yen Xen
	#       Power-down  0	   -   -   -
	#       Sleep       1	   0   0   0
	#       Normal      1    -   -   - 
	
	
	def setCTRL_REG1(self, val):
		"""Set register CTRL_REG1"""
		self.write(REG.CTRL_REG1, val, 8)
	
	def getCTRL_REG1(self):
		"""Get register CTRL_REG1"""
		return self.read(REG.CTRL_REG1, 8)
	
	# Bits DR
	# DR1-DR0: Output data rate selection. Refer to Table 22 
	#           DR<1:0> is used to set ODR selection. 
	
	# Bits BW
	# Bandwidth selection. Refer to Table 22
	#           BW <1:0> is used to set Bandwidth selection. 
	
	# Bits PD
	# Power-down mode enable.
	# Bits Zen
	# Z-axis enable. 
	# Bits Yen
	# Y-axis enable. 
	# Bits Xen
	# X-axis enable. 
	# Register CTRL_REG2
	# 7.3
	#       1.   Value loaded at boot. 
	
	
	def setCTRL_REG2(self, val):
		"""Set register CTRL_REG2"""
		self.write(REG.CTRL_REG2, val, 8)
	
	def getCTRL_REG2(self):
		"""Get register CTRL_REG2"""
		return self.read(REG.CTRL_REG2, 8)
	
	# Bits reserved_0
	# These values must not be changed. 
	# Bits HPM1
	# High-pass filter mode selection. 
	# Bits HPCF
	# High-pass filter cut-off frequency selection 
	#           Table 27.     High-pass filter cut-off frequency configuration [Hz]
	#                 -----ODR/Hz----
	#           HPCF  100 200   400  800
	#           0000	8     15   30   56
	#           0001	4      8    5   30
	#           0010	2      4    8   15
	#           0011	1      2    4    8
	#           0100	0.5    1    2    4
	#           0101	0.2	 0.5    1    2
	#           0110	0.1	 0.2  0.5    1
	#           0111	0.05 0.1  0.2  0.5
	#           1000	0.02 0.05 0.1  0.2
	#           1001	0.01 0.02 0.05 0.1 
	
	# Register CTRL_REG3
	# 7.4 
	
	def setCTRL_REG3(self, val):
		"""Set register CTRL_REG3"""
		self.write(REG.CTRL_REG3, val, 8)
	
	def getCTRL_REG3(self):
		"""Get register CTRL_REG3"""
		return self.read(REG.CTRL_REG3, 8)
	
	# Bits I1_Int1
	# Interrupt enable on the INT1 pin. 
	# Bits I1_Boot
	# Boot status available on INT1. 
	# Bits H_Lactive
	# Interrupt active configuration on INT1. 
	# Bits PP_OD
	# Push-pull / open drain. 
	# Bits I2_DRDY
	# Date ready on DRDY/INT2. 
	# Bits I2_WTM
	# FIFO watermark interrupt on DRDY/INT2. 
	# Bits I2_ORun
	# FIFO overrun interrupt on DRDY/INT2. 
	# Bits I2_Empty
	# FIFO empty interrupt on DRDY/INT2. 
	# Register CTRL_REG4
	# 7.5 
	
	def setCTRL_REG4(self, val):
		"""Set register CTRL_REG4"""
		self.write(REG.CTRL_REG4, val, 8)
	
	def getCTRL_REG4(self):
		"""Get register CTRL_REG4"""
		return self.read(REG.CTRL_REG4, 8)
	
	# Bits unused_0
	# Bits BLE
	# Big/little endian data selection. 
	# Bits unused_1
	# Bits ST
	# Self-test enable. 
	# Bits SIM
	# SPI serial interface mode selection. 
	# Register CTRL_REG5
	# 7.6 
	
	def setCTRL_REG5(self, val):
		"""Set register CTRL_REG5"""
		self.write(REG.CTRL_REG5, val, 8)
	
	def getCTRL_REG5(self):
		"""Get register CTRL_REG5"""
		return self.read(REG.CTRL_REG5, 8)
	
	# Bits BOOT
	# Reboot memory content. 
	# Bits FIFO_EN
	# FIFO enable. 
	# Bits unused_0
	# Bits HPen
	# High-pass filter enable. 
	# Bits INT1_Sel
	# INT1 selection configuration. (see Figure 19) 
	#           Table 36.     INT_SEL configuration settings
	#           Hpen  INT_SEL1  INT_SEL2	Description
	#           x     0         0         Non-high-pass-filtered data are used for interrupt generation
	#           x     0         1         High-pass-filtered data are used for interrupt generation
	#           0     1         x         Low-pass-filtered data are used for interrupt generation
	#           1     1         x         High-pass and low-pass-filtered data are used for interrupt generation 
	
	# Bits Out_Sel
	# Out selection configuration. (see Figure 19)
	#           Table 35.     Out_Sel configuration settings
	#           Hpen	OUT_SEL1 OUT_SEL0 Description
	#           x	    0        0        Data in DataReg and FIFO are non-high- pass-filtered
	#           x     0        1        Data in DataReg and FIFO are high-pass- filtered
	#           0     1        x        Data in DataReg and FIFO are low-pass- filtered by LPF2
	#           1     1        x        Data in DataReg and FIFO are high-pass and low-pass-filtered by LPF2 
	
	# Register REFERENCE
	# 7.7 REFERENCE/DATACAPTURE 
	#       Reference value for interrupt generation. 
	
	
	def setREFERENCE(self, val):
		"""Set register REFERENCE"""
		self.write(REG.REFERENCE, val, 8)
	
	def getREFERENCE(self):
		"""Get register REFERENCE"""
		return self.read(REG.REFERENCE, 8)
	
	# Bits REFERENCE
	# Register OUT_TEMP
	# 7.8 
	#       Temperature data. 
	
	
	def setOUT_TEMP(self, val):
		"""Set register OUT_TEMP"""
		self.write(REG.OUT_TEMP, val, 8)
	
	def getOUT_TEMP(self):
		"""Get register OUT_TEMP"""
		return self.read(REG.OUT_TEMP, 8)
	
	# Bits OUT_TEMP
	# Register STATUS_REG
	# 7.9 
	
	def setSTATUS_REG(self, val):
		"""Set register STATUS_REG"""
		self.write(REG.STATUS_REG, val, 8)
	
	def getSTATUS_REG(self):
		"""Get register STATUS_REG"""
		return self.read(REG.STATUS_REG, 8)
	
	# Bits ZYXOR
	# X, Y, Z-axis data overrun. 
	# Bits ZOR
	# Z-axis data overrun. 
	# Bits YOR
	# Y-axis data overrun. 
	# Bits XOR
	# X-axis data overrun. 
	# Bits ZYXDA
	# X, Y, Z-axis new data available. 
	# Bits ZDA
	# Z-axis new data available. 
	# Bits YDA
	# Y-axis new data available. 
	# Bits XDA
	# X-axis new data available. 
	# Register OUT_X_L
	# 7.10
	#       X-axis angular rate data. The value is expressed as 2’s complement. 
	
	
	def setOUT_X_L(self, val):
		"""Set register OUT_X_L"""
		self.write(REG.OUT_X_L, val, 8)
	
	def getOUT_X_L(self):
		"""Get register OUT_X_L"""
		return self.read(REG.OUT_X_L, 8)
	
	# Bits OUT_X_L
	# Register OUT_Y_L
	# 7.11
	#       Y-axis angular rate data. The value is expressed as 2’s complement. 
	
	
	def setOUT_Y_L(self, val):
		"""Set register OUT_Y_L"""
		self.write(REG.OUT_Y_L, val, 8)
	
	def getOUT_Y_L(self):
		"""Get register OUT_Y_L"""
		return self.read(REG.OUT_Y_L, 8)
	
	# Bits OUT_Y_L
	# Register OUT_Z_L
	# 7.12
	#       Z-axis angular rate data. The value is expressed as 2’s complement. 
	
	
	def setOUT_Z_L(self, val):
		"""Set register OUT_Z_L"""
		self.write(REG.OUT_Z_L, val, 8)
	
	def getOUT_Z_L(self):
		"""Get register OUT_Z_L"""
		return self.read(REG.OUT_Z_L, 8)
	
	# Bits OUT_Z_L
	# Register FIFO_CTRL_REG
	# 7.13 
	
	def setFIFO_CTRL_REG(self, val):
		"""Set register FIFO_CTRL_REG"""
		self.write(REG.FIFO_CTRL_REG, val, 8)
	
	def getFIFO_CTRL_REG(self):
		"""Get register FIFO_CTRL_REG"""
		return self.read(REG.FIFO_CTRL_REG, 8)
	
	# Bits FM
	# FIFO mode selection. 
	# Bits WTM
	# FIFO threshold. Watermark level setting 
	# Register FIFO_SRC_REG
	# 7.14 
	
	def setFIFO_SRC_REG(self, val):
		"""Set register FIFO_SRC_REG"""
		self.write(REG.FIFO_SRC_REG, val, 8)
	
	def getFIFO_SRC_REG(self):
		"""Get register FIFO_SRC_REG"""
		return self.read(REG.FIFO_SRC_REG, 8)
	
	# Bits WTM
	# Watermark status. 
	# Bits OVRN
	# Bits EMPTY
	# FIFO empty bit 
	# Bits FSS
	# FIFO stored data level 
	# Register INT1_CFG
	# 7.15 
	#       Configuration register for interrupt source. 
	
	
	def setINT1_CFG(self, val):
		"""Set register INT1_CFG"""
		self.write(REG.INT1_CFG, val, 8)
	
	def getINT1_CFG(self):
		"""Get register INT1_CFG"""
		return self.read(REG.INT1_CFG, 8)
	
	# Bits AND_OR
	# AND/OR combination of interrupt events. 
	# Bits LIR
	# Latch interrupt request. 
	# Bits ZHIE
	# Enable interrupt generation on Z high event. 
	# Bits ZLIE
	# Enable interrupt generation on Z low event. 
	# Bits YHIE
	# Enable interrupt generation on Y high event. 
	# Bits YLIE
	# Enable interrupt generation on Y low event. 
	# Bits XHIE
	# Enable interrupt generation on X high event. 
	# Bits XLIE
	# Enable interrupt generation on X low event. 
	# Register INT1_SRC
	# 7.16
	#       Interrupt source register. 
	#       Reading at this address clears the INT1_SRC IA bit (and eventually the interrupt signal on the INT1 pin) 
	#       and allows the refreshment of data in the INT1_SRC register if the latched option is chosen. 
	
	
	def setINT1_SRC(self, val):
		"""Set register INT1_SRC"""
		self.write(REG.INT1_SRC, val, 8)
	
	def getINT1_SRC(self):
		"""Get register INT1_SRC"""
		return self.read(REG.INT1_SRC, 8)
	
	# Bits unused_0
	# Bits IA
	# Interrupt active. 
	# Bits ZH
	# Z high. 
	# Bits ZL
	# Z low. 
	# Bits YH
	# Y high. 
	# Bits YL
	# Y low. 
	# Bits XH
	# X high. 
	# Bits XL
	# X low. 
	# Register INT1_THS_XH
	# 7.17
	#       Table 53.     INT1_THS_XH description
	#       THSX14 - THSX9     Interrupt threshold. Default value: 0000 0000 
	
	
	def setINT1_THS_XH(self, val):
		"""Set register INT1_THS_XH"""
		self.write(REG.INT1_THS_XH, val, 8)
	
	def getINT1_THS_XH(self):
		"""Get register INT1_THS_XH"""
		return self.read(REG.INT1_THS_XH, 8)
	
	# Bits INT1_THS_XH
	# Register INT1_THS_XL
	# 7.18
	#       Interrupt threshold. 
	
	
	def setINT1_THS_XL(self, val):
		"""Set register INT1_THS_XL"""
		self.write(REG.INT1_THS_XL, val, 8)
	
	def getINT1_THS_XL(self):
		"""Get register INT1_THS_XL"""
		return self.read(REG.INT1_THS_XL, 8)
	
	# Bits INT1_THS_XL
	# Register INT1_THS_YH
	# 7.19
	#       Interrupt threshold. 
	
	
	def setINT1_THS_YH(self, val):
		"""Set register INT1_THS_YH"""
		self.write(REG.INT1_THS_YH, val, 8)
	
	def getINT1_THS_YH(self):
		"""Get register INT1_THS_YH"""
		return self.read(REG.INT1_THS_YH, 8)
	
	# Bits INT1_THS_YH
	# Register INT1_THS_YL
	# 7.20
	#       Interrupt threshold. 
	
	
	def setINT1_THS_YL(self, val):
		"""Set register INT1_THS_YL"""
		self.write(REG.INT1_THS_YL, val, 8)
	
	def getINT1_THS_YL(self):
		"""Get register INT1_THS_YL"""
		return self.read(REG.INT1_THS_YL, 8)
	
	# Bits INT1_THS_YL
	# Register INT1_THS_ZH
	# 7.21
	#       Interrupt threshold. 
	
	
	def setINT1_THS_ZH(self, val):
		"""Set register INT1_THS_ZH"""
		self.write(REG.INT1_THS_ZH, val, 8)
	
	def getINT1_THS_ZH(self):
		"""Get register INT1_THS_ZH"""
		return self.read(REG.INT1_THS_ZH, 8)
	
	# Bits INT1_THS_ZH
	# Register INT1_THS_ZL
	# 7.22
	#       Interrupt threshold. 
	
	
	def setINT1_THS_ZL(self, val):
		"""Set register INT1_THS_ZL"""
		self.write(REG.INT1_THS_ZL, val, 8)
	
	def getINT1_THS_ZL(self):
		"""Get register INT1_THS_ZL"""
		return self.read(REG.INT1_THS_ZL, 8)
	
	# Bits INT1_THS_ZL
