<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">

# ICS3204 COMPUTER GRAPHICS CAT 1 PROJECT

## Introduction

This is an introduction to your project.

## Project Installation

To install this project, follow these steps:

1. Clone this repository:

   ```bash
   git clone <repository_name> <folder_name>
   <button class="copy-button" onclick="copyCode()">
       <i class="fas fa-copy"></i> Copy
   </button>

   ```

2. Download the massive dataset. The massive dataset 1.1 can be downloaded <a href="https://amazon-massive-nlu-dataset.s3.amazonaws.com/amazon-massive-dataset-1.1.tar.gz">here<a>.

<script>
function copyCode() {
    const codeBlock = document.querySelector('pre code');
    const textArea = document.createElement('textarea');
    textArea.value = codeBlock.innerText;
    document.body.appendChild(textArea);
    textArea.select();
    document.execCommand('copy');
    document.body.removeChild(textArea);
}
</script>
<style>
.code-container {
    position: relative;
    border: 1px solid #ccc;
    padding: 10px;
    border-radius: 4px;
    margin-bottom: 20px;
}

.copy-button {
    position: relative;
    margin-left: 10px;
    background: none;
    border: none;
    cursor: pointer;
    color: #007bff; /* Customize the color as needed */
}
</style>
