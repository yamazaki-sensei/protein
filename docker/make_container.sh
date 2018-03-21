mkdir -p temp
cp -fr ../server ./temp
docker build -t protein_server .
