import time
import chipwhisperer as cw


def cwconnect(offset=1250, totalsamples=3000):
    scope = cw.scope()
    target = cw.target(scope)

    # setup scope parameters
    scope.gain.gain = 45
    scope.adc.samples = int(totalsamples)
    scope.adc.offset = int(offset)
    scope.adc.basic_mode = "rising_edge"
    scope.clock.clkgen_freq = 7370000
    scope.clock.adc_src = "clkgen_x4"
    scope.trigger.triggers = "tio4"
    scope.io.tio1 = "serial_rx"
    scope.io.tio2 = "serial_tx"
    scope.io.hs2 = "clkgen"

    return (cw, scope, target)


def measure_AES(scope, target, plaintext, key):
    plaintext = [int(p) for p in plaintext]
    key = [int(k) for k in key]

    target.reinit()

    target.setModeEncrypt()  # only does something for targets that support it
    target.loadEncryptionKey(key)
    target.loadInput(plaintext)

    # run aux stuff that should run before the scope arms here

    scope.arm()

    # run aux stuff that should run after the scope arms here

    target.go()
    timeout = 50
    # wait for target to finish
    while target.isDone() is False and timeout:
        timeout -= 1
        time.sleep(0.01)

    try:
        ret = scope.capture()
        if ret:
            print('Timeout happened during acquisition')
    except IOError as e:
        print('IOError: %s' % str(e))

    # run aux stuff that should happen after trace here

    trace = list(scope.getLastTrace())
    textout = list(target.readOutput())

    return (textout, trace)
