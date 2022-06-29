# MSSQL ARM64

This repo aims to demonstrate how SQL Server can be used with ARM64 processor
architectures in combination with `sqlcmd` in Docker as Microsoft up until this date
(06-29-2022) has no native support for either SQL Server or `sqlcmd` for ARM
processors like Apple Silicon (M1, M2) etc.

## Usage

The Dockerfile extends the [`mcr.microsoft.com/azure-sql-edge`](https://hub.docker.com/_/microsoft-azure-sql-edge)
image and installs the golang port of [`sqlcmd`](https://github.com/microsoft/go-sqlcmd).

The `docker-compose.yml` file demonstrates how a simple containerized Python
application located in `/example` can wait for the SQL server to be ready
before it connects.
