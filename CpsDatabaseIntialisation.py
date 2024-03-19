import sqlite3

connect = sqlite3.connect('CompletePropertySolutions.db')
cursor = connect.cursor()

# Creating tblTenants
cursor.execute('''CREATE TABLE IF NOT EXISTS tblTenants (
    tenantID INTEGER PRIMARY KEY,
    tenantFirstName TEXT,
    tenantSurname TEXT,
    dateOfBirth TEXT,
    tenantEmail TEXT,
    tenantMobile TEXT,
    tenancyStartDate TEXT,
    tenancyEndDate TEXT,
    tenantRentAmount REAL,
    propertyID INTEGER,
    FOREIGN KEY (propertyID) REFERENCES tblProperties(propertyID)
)''')

# Creating tblProperties
cursor.execute('''CREATE TABLE IF NOT EXISTS tblProperties (
    propertyID INTEGER PRIMARY KEY,
    propertyHouseNo INTEGER,
    propertyStreet TEXT,
    propertyTown TEXT,
    propertyPostCode TEXT,
    propertyValue TEXT,
    propertyDateListed TEXT,
    propertyStatus TEXT,
    numberOfBedrooms INTEGER,
    propertyType TEXT,
    yearBuilt INTEGER,
    landlordID INTEGER,
    FOREIGN KEY (landlordID) REFERENCES tblLandlords(landlordID)
)''')

# Creating tblLandlords
cursor.execute('''CREATE TABLE IF NOT EXISTS tblLandlords (
    landlordID INTEGER PRIMARY KEY,
    landlordFirstName TEXT,
    landlordSurname TEXT,
    landlordMobile TEXT,
    landlordHouseNo INTEGER,
    landlordStreet TEXT,
    landlordTown TEXT,
    landlordPostCode TEXT
)''')
