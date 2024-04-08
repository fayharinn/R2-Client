import mimetypes

mime_types = {
    # Image formats
    '.png': 'image/png',
    '.jpg': 'image/jpeg',
    '.jpeg': 'image/jpeg',
    '.gif': 'image/gif',
    '.svg': 'image/svg+xml',  # Scalable Vector Graphics
    '.ico': 'image/x-icon',    # Icon file format

    # Audio formats
    '.m4a': 'audio/x-m4a',
    '.mp3': 'audio/mpeg',
    '.wav': 'audio/wav',
    '.ogg': 'audio/ogg',       # Ogg audio format

    # Video formats
    '.mp4': 'video/mp4',
    '.avi': 'video/x-msvideo',
    '.mov': 'video/quicktime',
    '.flv': 'video/x-flv',
    '.wmv': 'video/x-ms-wmv',
    '.webm': 'video/webm',     # WebM video format

    # Document formats
    '.pdf': 'application/pdf',
    '.doc': 'application/msword',
    '.docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
    '.ppt': 'application/vnd.ms-powerpoint',
    '.pptx': 'application/vnd.openxmlformats-officedocument.presentationml.presentation',
    '.xls': 'application/vnd.ms-excel',
    '.xlsx': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    '.txt': 'text/plain',

    # Web formats
    '.html': 'text/html',
    '.css': 'text/css',
    '.js': 'application/javascript',
    '.json': 'application/json',
    '.xml': 'application/xml',

    # Other formats
    '.csv': 'text/csv',
    '.zip': 'application/zip',
    '.tar': 'application/x-tar',
    '.gz': 'application/gzip',
    '.rar': 'application/vnd.rar',
    '.7z': 'application/x-7z-compressed',
    '.eps': 'application/postscript',  # Encapsulated PostScript format
    '.sql': 'application/sql',         # SQL files
    '.java': 'text/x-java-source',      # Java source code
    # Add more mappings as needed
}


def get_content_type(file_key):
    """
    Determine the MIME type based on the file extension using the mimetypes module.

    :param file_key: The file key or file name from which to extract the extension.
    :return: The MIME type as a string, defaults to 'application/octet-stream' if not detected.
    """
      # Try to get the MIME type from the provided dictionary
    mime_type = mime_types.get("."+file_key.split(".")[-1].lower())
    if mime_type:
        return mime_type

    # If not found in the provided dictionary, use the mimetypes module
    mime_type, _ = mimetypes.guess_type(file_key)
    return mime_type if mime_type is not None else 'application/octet-stream'