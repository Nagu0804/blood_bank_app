    <h1>Blood Bank App Readme</h1>

    <h2>Overview</h2>

    <p>This is a blood bank application designed to manage blood donation and distribution. The application is containerized using Docker for easy deployment and scalability. Follow the instructions below to set up and run the Blood Bank App on your local machine.</p>

    <h2>Prerequisites</h2>

    <ul>
        <li>Docker installed on your machine (<a href="https://docs.docker.com/get-docker/">Install Docker</a>)</li>
    </ul>

    <h2>Installation</h2>

    <ol>
        <li><strong>Clone the repository:</strong></li>

        <pre><code>git clone https://github.com/your-username/blood_bank_app.git
cd blood_bank_app
        </code></pre>

        <li><strong>Build the Docker image:</strong></li>

        <pre><code>docker build -t &lt;app_name&gt; .
        </code></pre>

        <li><strong>Run the Docker container:</strong></li>

        <pre><code>docker run -p 8000:8000 &lt;app_name&gt;
        </code></pre>
    </ol>

    <h2>Database Migration</h2>

    <p>To set up the database inside the container, follow these steps:</p>

    <ol>
        <li><strong>Access the container shell:</strong></li>

        <pre><code>docker exec -it CONTAINER_NAME_OR_ID /bin/bash
        </code></pre>

        <li><strong>Run migrations:</strong></li>

        <pre>  
            <code>
                python3 manage.py makemigrations
                python3 manage.py migrate
            </code>
        </pre>
    </ol>

    <h2>Access the Application</h2>

    <p>Once the container is running and the database is migrated, access the Blood Bank App through your web browser:</p>

    <ul>
        <li><a href="http://localhost:8000">http://localhost:8000</a></li>
        <li><a href="http://127.0.0.1:8000">http://127.0.0.1:8000</a></li>
        <li><a href="http://0.0.0.0:8000">http://0.0.0.0:8000</a></li>
    </ul>

    <h2>Usage</h2>

    <p>Explore the Blood Bank App to manage blood donations and distributions. You can perform various operations like adding donors, tracking available blood types, and managing requests.</p>

    <h2>Contributing</h2>

    <p>If you'd like to contribute to the Blood Bank App, please follow the standard contribution guidelines of the project.</p>

    <h2>License</h2>

    <p>This Blood Bank App is open-source and distributed under the <a href="LICENSE">MIT License</a>.</p>

    <p>Feel free to contact us for any issues or improvements!</p>
