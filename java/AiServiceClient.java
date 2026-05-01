import org.springframework.web.client.RestTemplate;
import org.springframework.web.client.RestClientException;
import org.springframework.http.client.SimpleClientHttpRequestFactory;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import java.util.Map;
import java.util.HashMap;

public class AiServiceClient {

    private final RestTemplate restTemplate;
    private final String baseUrl;

    public AiServiceClient(String baseUrl) {
        this.baseUrl = baseUrl;
        this.restTemplate = new RestTemplate();
        SimpleClientHttpRequestFactory factory = new SimpleClientHttpRequestFactory();
        factory.setReadTimeout(10000); // 10 seconds
        factory.setConnectTimeout(10000); // 10 seconds
        this.restTemplate.setRequestFactory(factory);
    }

    public String test() {
        try {
            ResponseEntity<String> response = restTemplate.getForEntity(baseUrl + "/test", String.class);
            return response.getBody();
        } catch (RestClientException e) {
            return null;
        }
    }

    public String describe(String prompt) {
        try {
            HttpHeaders headers = new HttpHeaders();
            headers.setContentType(MediaType.APPLICATION_JSON);
            Map<String, String> requestBody = new HashMap<>();
            requestBody.put("prompt", prompt);
            HttpEntity<Map<String, String>> entity = new HttpEntity<>(requestBody, headers);
            ResponseEntity<String> response = restTemplate.postForEntity(baseUrl + "/describe", entity, String.class);
            return response.getBody();
        } catch (RestClientException e) {
            return null;
        }
    }

    public String generateReport() {
        try {
            HttpHeaders headers = new HttpHeaders();
            headers.setContentType(MediaType.APPLICATION_JSON);
            Map<String, Object> requestBody = new HashMap<>();
            HttpEntity<Map<String, Object>> entity = new HttpEntity<>(requestBody, headers);
            ResponseEntity<String> response = restTemplate.postForEntity(baseUrl + "/generate-report", entity, String.class);
            return response.getBody();
        } catch (RestClientException e) {
            return null;
        }
    }
}