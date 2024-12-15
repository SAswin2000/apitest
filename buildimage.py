
name: Build and Push Docker Image

 

on:

  push:

    branches:

      - branch2

  pull_request:

    branches:

      - branch2

 

jobs:

  build:

    runs-on: ubuntu-latest

 

    steps:

     

      - name: Checkout code

        uses: actions/checkout@v3

 

     

      - name: Log in to GitHub Container Registry

        uses: docker/login-action@v2

        with:

          registry: ghcr.io

          username: ${{ github.actor }}

          password: ${{ secrets.GITHUB_TOKEN }}

 

     

      - name: Build Docker image

        run: |

          docker build ghcr.io/${{ github.repository_owner }}/${{ github.repository }}:latest .

 

     

      - name: Push Docker image

        run: |

          docker push ghcr.io/${{ github.repository_owner }}/${{ github.repository }}:latest

 