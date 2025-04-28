import configparser


def readConfigData(section, key):
    config = configparser.ConfigParser()
    # Directly read the configuration file
    config.read("./ConfigurationFiles/Config.cfg")
  # Retrieve and return the value for the specified section and key
    return config.get(section, key)



def fetchelementLocators(section,key):
    config = configparser.ConfigParser()
    config.read("./ConfigurationFiles/Elements.cfg")
    return config.get(section, key)


