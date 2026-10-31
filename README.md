# Smart Moroccan Data Lake

A real-time geospatial data platform for Morocco. It collects live public signals (aircraft, weather, earthquakes), processes them through a lakehouse architecture, and serves both a live map and historical analytics.

> Status: in progress. Environment set up; ingestion (Milestone 1) under development.

## Architecture
Public APIs → Ingestion (Python) → Bronze (raw) → Silver (clean) → Quality checks → Gold (analytics) → Map & dashboard

## Tech stack
Python · PySpark · Delta Lake · DuckDB · pytest · AlmaLinux (WSL2)

## Roadmap
- [x] Environment and project structure
- [ ] Bronze ingestion
- [ ] Silver layer (Spark + Delta Lake)
- [ ] Data quality checks
- [ ] Gold layer and analytics
- [ ] Scheduling
- [ ] Map and data health dashboard