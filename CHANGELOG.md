# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial project setup for GitHub publication

## [1.0.0] - 2024-12-20

### Added
- MCP (Model Context Protocol) server for Elsevier APIs
- Scopus API integration for paper search
- SciVal API integration for author information
- Abstract Retrieval API for detailed paper metadata
- Research trend analysis functionality
- Institution paper statistics
- Open access paper search
- Comprehensive test suite
- Documentation and usage examples
- Cursor IDE configuration support

### Features
- **Paper Search**: Query academic papers by keywords, authors, and fields
- **Author Analysis**: Retrieve detailed researcher profiles and metrics
- **Research Trends**: Analyze year-over-year publication trends by field
- **Institution Statistics**: Get paper counts and metrics by institution
- **Open Access**: Search specifically for open access publications
- **Abstract Retrieval**: Fetch detailed abstracts and metadata

### APIs Integrated
- Scopus Search API
- SciVal Author Lookup API
- Abstract Retrieval API
- SciVal Analytics API

### Documentation
- Comprehensive README with setup instructions
- API usage examples
- Cursor IDE configuration guide
- Contributing guidelines
- MIT License

### Technical Details
- Python 3.7+ support
- JSON-RPC 2.0 MCP protocol implementation
- Error handling and rate limiting
- Environment variable configuration
- Cross-platform compatibility

### Testing
- Complete API endpoint testing
- Integration tests with live Elsevier APIs
- Example usage scripts
- CI/CD ready structure

---

## How to Update This Changelog

When making changes to this project:

1. Add new entries under `[Unreleased]`
2. Use the following categories:
   - `Added` for new features
   - `Changed` for changes in existing functionality
   - `Deprecated` for soon-to-be removed features
   - `Removed` for now removed features
   - `Fixed` for any bug fixes
   - `Security` in case of vulnerabilities

3. When releasing, move items from `[Unreleased]` to a new version section
4. Add a release date in YYYY-MM-DD format