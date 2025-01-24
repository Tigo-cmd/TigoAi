#!/usr/bin/env bash
# handles the package installation

if [ "$(id -u)" != "0" ]
then
  echo "sorry, you are not root."
  exit 1
fi

clear -x

MAIN_FILE="Tigo"
REQUIREMENTS="models"
REQUIREMENTS1=".env"

PROJECT_PATH="/opt/Tigo"
BIN_PATH="/usr/local/bin/"
MAN_PATH="/usr/local/share/man/man1/"

echo -e "Installing Binaries..."
sleep 09
mkdir -p "${PROJECT_PATH}"


cp "${MAIN_FILE}.py" "${PROJECT_PATH}/${MAIN_FILE}"
cp -r "${REQUIREMENTS}" "${PROJECT_PATH}"
cp -r "${REQUIREMENTS1}" "${PROJECT_PATH}"

echo -e "Making Executables"
sleep 03

chmod +x "${PROJECT_PATH}/${MAIN_FILE}"

ln -s "${PROJECT_PATH}/${MAIN_FILE}" "${BIN_PATH}/${MAIN_FILE}"

echo -e "Installing man pages.."

cp "man/sc.1" "${MAN_PATH}"

echo -e "Updating man database.."
sleep 03

mandb

echo -e "All set Run 'Tigo -h' for help or 'man Tigo' for more info "


