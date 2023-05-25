-- Create the 'person' table
CREATE TABLE person (
  id INTEGER PRIMARY KEY,
  name TEXT,
  age INTEGER,
  gender TEXT
);

-- Create the 'location' table
CREATE TABLE location (
  id INTEGER PRIMARY KEY,
  country TEXT,
  province TEXT,
  latitude REAL,
  longitude REAL
);

-- Create the 'store' table
CREATE TABLE store (
  id INTEGER PRIMARY KEY,
  name TEXT,
  location_id INTEGER,
  rating INTEGER,
  FOREIGN KEY (location_id) REFERENCES location(id)
);

-- Create the 'product' table
CREATE TABLE product (
  id INTEGER PRIMARY KEY,
  name TEXT,
  category TEXT,
  price REAL,
  store_id INTEGER,
  rating INTEGER,
  FOREIGN KEY (store_id) REFERENCES store(id)
);

-- Create the 'price' table
CREATE TABLE price (
  id INTEGER PRIMARY KEY,
  product_id INTEGER,
  price REAL,
  date DATE,
  FOREIGN KEY (product_id) REFERENCES product(id)
);
