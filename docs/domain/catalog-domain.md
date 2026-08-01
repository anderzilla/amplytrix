# Product Catalog domain

Owns Product, CatalogItem/Version, Feature, Plan/Version, Price and Add-on. Invariants: stable identities; published versions are immutable; effective windows do not overlap for the same market selector; prices use integer minor units plus ISO currency; retirement names a replacement where applicable. It publishes versioned catalog snapshots; it does not authorize access or execute items.
