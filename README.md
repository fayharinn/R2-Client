
# R2Client

`R2Client` is a Python client library for interacting with Cloudflare R2 storage, facilitating easy and quick HTTP requests to manage files within an R2 bucket. This framework leverages Python's native packages to sign and send requests, making it straightforward to integrate into existing Python projects.

## Features

- File upload and download
- Listing files and folders within a bucket

## Installation

To install `r2client`, simply use pip:

```
pip install r2client
```

## Quick Start

Here's how to get started with `r2client`:

### Setting Up

First, import `R2Client` and initialize it with your credentials:

```python
from r2client import R2Client

# Initialize the R2Client
client = R2Client(
    access_key='<ACCESS_KEY>',
    secret_key='<SECRET_KEY>',
    endpoint='<ENDPOINT> (example: "https://***.r2.cloudflarestorage.com")'
)
```

### Uploading a File

To upload a file to your R2 bucket:

```python
bucket_name = 'your-bucket-name'
local_file_path = 'path/to/your/local/file'
r2_file_key = 'desired/path/in/bucket'

client.upload_file(bucket_name, local_file_path, r2_file_key)
```

### Downloading a File

To download a file from your R2 bucket:

```python
file_key = 'path/to/the/file/in/bucket'
local_file_name = 'path/to/save/the/downloaded/file'

client.download_file(bucket_name, file_key, local_file_name)
```

### Listing Files

To list files in a specific bucket:

```python
files_dict = client.list_files(bucket_name)
print(files_dict)
```

### Listing Folders

To list folders within a bucket:

```python
folders = client.list_folders(bucket_name)
print(folders)
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or create an issue for any bugs or feature requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
