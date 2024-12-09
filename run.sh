GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

set -e

command -v python3 >/dev/null 2>&1 || { echo >&2 "Python3 is required but not installed.  Aborting."; exit 1; }
command -v virtualenv >/dev/null 2>&1 || { python3 -m pip install --user virtualenv; }
command -v mysql >/dev/null 2>&1 || { echo >&2 "MySQL is required but not installed.  Aborting."; exit 1; }


createWebStructure() {
    echo -e "${YELLOW}🏗️ Creating Web Directory Structure${NC}"

    # Create main roots
    mkdir index.html .gitignore .env
    mkdir -p {static/{css,js,img},templates} || { echo "Error creating directories"; exit 1; }

    # Create placeholder files for static
    touch static/{dash.css, file.css} || { echo "Error creating static directories"; exit 1; }

    # Create placeholder files for templates
    touch templates/{dashboard.html,filesdata.html,readfiles.html} || { echo "Error creating templates directories"; exit 1; }
}