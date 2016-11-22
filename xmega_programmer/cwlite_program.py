#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2013-2014, NewAE Technology Inc
# All rights reserved.
#
# Authors: Colin O'Flynn
#
# Find this and more at newae.com - this file is part of the chipwhisperer
# project, http://www.assembla.com/spaces/chipwhisperer
#
#    This file is part of chipwhisperer.
#
#    chipwhisperer is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    chipwhisperer is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with chipwhisperer.  If not, see <http://www.gnu.org/licenses/>.
#=================================================

import sys, os
from chipwhisperer.common.api.CWCoreAPI import CWCoreAPI  # Import the ChipWhisperer API
from chipwhisperer.common.scripts.base import UserScriptBase
from chipwhisperer.hardware.naeusb.naeusb import NAEUSB
from chipwhisperer.hardware.naeusb.programmer_xmega import XMEGAPDI, XMEGA128D4
from chipwhisperer.capture.utils.XMEGAProgrammer import XMEGAProgrammer


class UserScript(UserScriptBase):
    _name = "ChipWhisperer-Lite: AES SimpleSerial on XMEGA"
    _description = "SimpleSerial with Standard Target for AES (XMEGA)"

    def __init__(self, api):
        super(UserScript, self).__init__(api)

    def run(self):
        # User commands here
        self.api.setParameter(['Generic Settings', 'Scope Module', 'ChipWhisperer/OpenADC'])
        self.api.setParameter(['Generic Settings', 'Target Module', 'Simple Serial'])
        self.api.setParameter(['Generic Settings', 'Trace Format', 'ChipWhisperer/Native'])
        self.api.setParameter(['Simple Serial', 'Connection', 'NewAE USB (CWLite/CW1200)'])
        self.api.setParameter(['ChipWhisperer/OpenADC', 'Connection', 'NewAE USB (CWLite/CW1200)'])
                
        self.api.connect()
        
        # Example of using a list to set parameters. Slightly easier to copy/paste in this format
        lstexample = [['CW Extra Settings', 'Trigger Pins', 'Target IO4 (Trigger Line)', True],
                      ['CW Extra Settings', 'Target IOn Pins', 'Target IO1', 'Serial RXD'],
                      ['CW Extra Settings', 'Target IOn Pins', 'Target IO2', 'Serial TXD'],
                      ['OpenADC', 'Clock Setup', 'CLKGEN Settings', 'Desired Frequency', 7370000.0],
                      ['CW Extra Settings', 'Target HS IO-Out', 'CLKGEN'],
                      ['OpenADC', 'Clock Setup', 'ADC Clock', 'Source', 'CLKGEN x4 via DCM'],
                      ['OpenADC', 'Trigger Setup', 'Total Samples', 3000],
                      ['OpenADC', 'Trigger Setup', 'Offset', 1250],
                      ['OpenADC', 'Trigger Setup', 'Mode', 'rising edge'],
                      ['OpenADC', 'Gain Setting', 'Setting', 45],
                      # Final step: make DCMs relock in case they are lost
                      ['OpenADC', 'Clock Setup', 'ADC Clock', 'Reset ADC DCM', None],
                      ]
        
        # Download all hardware setup parameters
        for cmd in lstexample: self.api.setParameter(cmd)
        
if __name__ == '__main__':

    if len(sys.argv) > 1:
        useGUI = False
    else:
        useGUI = True
        print "usage: %s [hexfile]"%sys.argv[0]
        print "  If no hexfile specified, opens GUI"
        print "  If hex-file specified, programs without opening GUI"

    if useGUI:
        import chipwhisperer.capture.ui.CWCaptureGUI as cwc         # Import the ChipWhispererCapture GUI
        from chipwhisperer.common.utils.parameter import Parameter  # Comment this line if you don't want to use the GUI
        Parameter.usePyQtGraph = True                               # Comment this line if you don't want to use the GUI
    api = CWCoreAPI()                                           # Instantiate the API
    
    if useGUI:
        app = cwc.makeApplication("Capture")                        # Change the name if you want a different settings scope
        gui = cwc.CWCaptureGUI(api)                                 # Comment this line if you don't want to use the GUI
    api.runScriptClass(UserScript)                              # Run the User Script (executes "run()" by default)
    
    #System should now be setup (assuming CW-Lite found). Do programming if hex-file specified, otherwise open GUI
    if useGUI:
        from PySide.QtGui import *
        for act in gui._ToolMenuItems:
            if act.text() == "CW-Lite XMEGA Programmer":
                act.activate(QAction.Trigger)
    else:   
        usb = api.getScope().scopetype.dev._cwusb
        _xmega = XMEGAPDI(usb)
        xmega = XMEGAProgrammer()
        xmega.setUSBInterface(_xmega)
        xmega.find()
        
        fname = sys.argv[1]
        print("Attempting to program %s to XMEGA"%fname)
        
        if os.path.isfile(fname):
            xmega.erase()
            xmega.program(fname)
        else:
            print("***** SPECIFIED FILE NOT FOUND ********")
            
        xmega.close()

        
    if useGUI:
        app.exec_()                                                 # Comment this line if you don't want to use the GUI
