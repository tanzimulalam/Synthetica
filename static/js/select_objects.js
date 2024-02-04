document.addEventListener('DOMContentLoaded', function() {
    const stixObjects = document.querySelectorAll('.stix-object');
    const selectedList = document.getElementById('selected-list');
    const generateGraphButton = document.getElementById('generate-graph');

    stixObjects.forEach(button => {
        button.addEventListener('click', function() {
            const objectName = this.getAttribute('data-object');
            if (this.classList.contains('selected')) {
                this.classList.remove('selected');
                removeEntityInput(objectName);
            } else {
                this.classList.add('selected');
                addEntityInput(objectName);
            }
        });
    });

    generateGraphButton.addEventListener('click', function() {
        const formData = new FormData();
        const inputs = selectedList.querySelectorAll('input');

        inputs.forEach(input => {
            formData.append(input.name, input.value);
        });

        fetch('/generate-graph', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            // Check if 'stix_bundle' is a string, and if so, parse it
            let bundleData = data.stix_bundle;
            if (typeof bundleData === 'string') {
                bundleData = JSON.parse(bundleData);
            }
            // Re-serialize with indentation for formatting
            document.getElementById('json-output').textContent = JSON.stringify(bundleData, null, 2);
        })
        .catch(error => console.error('Error:', error));
    });

    document.getElementById('copy-json').addEventListener('click', function() {
        const jsonOutput = document.getElementById('json-output').textContent;
        navigator.clipboard.writeText(jsonOutput).then(() => {
            alert('JSON copied to clipboard');
        }).catch(err => {
            console.error('Error in copying text: ', err);
        });
    });



    function addEntityInput(objectName) {
        const entityDiv = document.createElement('div');
        entityDiv.classList.add('entity');
        entityDiv.id = objectName + '-container';

        const label = document.createElement('label');
        label.htmlFor = `${objectName}-count`;
        label.textContent = `${capitalizeFirstLetter(objectName)} Count:`;

        const input = document.createElement('input');
        input.type = 'number';
        input.id = `${objectName}-count`;
        input.name = `${objectName}-count`;
        input.min = '1';

        entityDiv.appendChild(label);
        entityDiv.appendChild(input);
        selectedList.appendChild(entityDiv);
    }

    function removeEntityInput(objectName) {
        const entityDiv = document.getElementById(objectName + '-container');
        if (entityDiv) {
            selectedList.removeChild(entityDiv);
        }
    }

    function capitalizeFirstLetter(string) {
        return string.charAt(0).toUpperCase() + string.slice(1);
    }
});
