# HTTPS Deployment Configuration

To serve the Django application securely:

1. **Obtain SSL/TLS Certificate**

   - Use Let's Encrypt (free) or purchase a certificate.
   - Example with Certbot:
     ```bash
     sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com
     ```

2. **Configure Nginx for HTTPS**  
   Example `/etc/nginx/sites-available/libraryproject`:

   ```nginx
   server {
       listen 80;
       server_name yourdomain.com www.yourdomain.com;
       return 301 https://$host$request_uri;
   }

   server {
       listen 443 ssl;
       server_name yourdomain.com www.yourdomain.com;

       ssl_certificate /etc/letsencrypt/live/yourdomain.com/fullchain.pem;
       ssl_certificate_key /etc/letsencrypt/live/yourdomain.com/privkey.pem;

       location / {
           proxy_pass http://127.0.0.1:8000;
           proxy_set_header Host $host;
           proxy_set_header X-Forwarded-Proto https;
       }
   }
   ```
