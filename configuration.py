"""Contains transformer configuration information
"""

# The version number of the transformer
TRANSFORMER_VERSION = '3.0'

# The transformer description
TRANSFORMER_DESCRIPTION = 'MAC Met Station Weather DAT file parser'

# Short name of the transformer
TRANSFORMER_NAME = 'terra.environmental.weather_datparser'

# The sensor associated with the transformer
TRANSFORMER_SENSOR = 'weather_datparser'

# The transformer type (eg: 'rgbmask', 'plotclipper')
TRANSFORMER_TYPE = 'dat'

# The name of the author of the extractor
AUTHOR_NAME = 'Chris Schnaufer'

# The email of the author of the extractor
AUTHOR_EMAIL = 'schnaufer@email.arizona.edu'

# Contributors to this transformer
CONTRIBUTORS = ["Max Burnette <mburnet2@illinois.edu>"]

# Repository URI of where the source code lives
REPOSITORY = 'https://github.com/AgPipeline/transformer-weather_datparser.git'

# Hard-coded override of base docker image (used when Dockerfile is generated)
# If a name is entered here it will be used to populate the "FROM" field of the Dockerfile
BASE_DOCKER_IMAGE_OVERRIDE_NAME = ''
