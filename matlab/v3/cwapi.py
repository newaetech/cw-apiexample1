from chipwhisperer.common.api.CWCoreAPI import CWCoreAPI  # Import the ChipWhisperer API
import logging, time

def cwconnect(offset=1250, totalsamples=3000):

    api = CWCoreAPI()  # Instantiate the API


    api.setParameter(['Generic Settings', 'Scope Module', 'ChipWhisperer/OpenADC'])
    api.setParameter(['Generic Settings', 'Target Module', 'Simple Serial'])

    #No actual need for saving data so we ignore this?
    #api.setParameter(['Generic Settings', 'Trace Format', 'ChipWhisperer/Native'])

    api.setParameter(['Simple Serial', 'Connection', 'NewAE USB (CWLite/CW1200)'])
    api.setParameter(['ChipWhisperer/OpenADC', 'Connection', 'NewAE USB (CWLite/CW1200)'])

    api.connect()

    # Example of using a list to set parameters. Slightly easier to copy/paste in this format
    lstexample = [['CW Extra Settings', 'Trigger Pins', 'Target IO4 (Trigger Line)', True],
                  ['CW Extra Settings', 'Target IOn Pins', 'Target IO1', 'Serial RXD'],
                  ['CW Extra Settings', 'Target IOn Pins', 'Target IO2', 'Serial TXD'],
                  ['OpenADC', 'Clock Setup', 'CLKGEN Settings', 'Desired Frequency', 7370000.0],
                  ['CW Extra Settings', 'Target HS IO-Out', 'CLKGEN'],
                  ['OpenADC', 'Clock Setup', 'ADC Clock', 'Source', 'CLKGEN x4 via DCM'],
                  ['OpenADC', 'Trigger Setup', 'Total Samples', int(totalsamples)],
                  ['OpenADC', 'Trigger Setup', 'Offset', int(offset)],
                  ['OpenADC', 'Gain Setting', 'Setting', 45],
                  ['OpenADC', 'Trigger Setup', 'Mode', 'rising edge'],
                  # Final step: make DCMs relock in case they are lost
                  ['OpenADC', 'Clock Setup', 'ADC Clock', 'Reset ADC DCM', None],
                  ]

    # Download all hardware setup parameters
    for cmd in lstexample: api.setParameter(cmd)

    return api

def measure_AES(api, plaintext, key):

    #MATLAB loves it's floating point, just force everything to int in case
    plaintext = [int(p) for p in plaintext]
    key = [int(k) for k in key]


    target = api.getTarget()

    target.init()
    api.getScope().arm()

    target.reinit()
    target.setModeEncrypt()

    target.loadEncryptionKey(key)
    target.loadInput(plaintext)
    target.go()

    timeout = 50
    while target.isDone() == False and timeout:
        timeout -= 1
        time.sleep(0.01)

    if timeout == 0:
        raise IOError('Target timeout during acquisition - no data returned?')

    textout = target.readOutput()


    try:
        ret = api.getScope().capture()
        if ret:
            raise IOError('Scope timeout during acquisition - check clocks locked')
    except IOError as e:
        print('IOError: %s' % str(e))
        raise

    textout = list(textout)

    return (textout, api.getScope().channels[0].getTrace(0).tolist())