CREATE TABLE raw_fingerprints (
    fp_id serial PRIMARY KEY,
    raw_fingerprint varchar,
    fp_components text
);
