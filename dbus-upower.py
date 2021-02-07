import dbus

deviceTypes = ['Unknown',
'Line Power',
'Battery',
'UPS',
'Monitor',
'Mouse',
'Keyboard',
'PDA',
'Phone']

deviceStates = ['Unknown',
'Charging',
'Discharging',
'Emtpy',
'Fully Charged',
'Pending Charge',
'Pending Discharge']

# Get the system bus
bus = dbus.SystemBus()

# Access the UPower object and get an interface to it
upower_object = bus.get_object('org.freedesktop.UPower', '/org/freedesktop/UPower')
upower_interface = dbus.Interface(upower_object, 'org.freedesktop.UPower')

# Iterate over all UPower devices
for devicePath in upower_interface.EnumerateDevices():
    # Access the object and get a dbus properties interface to it
    device_object = bus.get_object('org.freedesktop.UPower', devicePath)
    properties_interface = dbus.Interface(device_object, 'org.freedesktop.DBus.Properties')

    # Extract the properties we're interested in
    deviceModel = properties_interface.Get('org.freedesktop.UPower.Device', 'Model')
    deviceType = deviceTypes[properties_interface.Get('org.freedesktop.UPower.Device', 'Type')]
    deviceState = deviceStates[properties_interface.Get('org.freedesktop.UPower.Device', 'State')]
    devicePercentage = properties_interface.Get('org.freedesktop.UPower.Device', 'Percentage')

    # Show result
    print(deviceModel, ' (', deviceType, ') ==> ', devicePercentage, '% ', deviceState, sep='')
