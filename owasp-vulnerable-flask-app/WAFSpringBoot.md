# WAF  Spring Boot

La configuration complète de Spring Security peut varier en fonction des besoins spécifiques de votre application, mais voici un exemple de configuration de base pour Spring Boot avec Spring Security. Ce code configure Spring Security pour protéger contre les attaques CSRF, autoriser l'accès à certaines ressources, gérer l'authentification, et plus encore.

Ajoutez ce fichier de configuration à votre projet Spring Boot. Par exemple, vous pouvez le placer dans le package config.

```java
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;
import org.springframework.security.web.authentication.UsernamePasswordAuthenticationFilter;

@Configuration
@EnableWebSecurity
public class SecurityConfig extends WebSecurityConfigurerAdapter {

    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http
            .addFilterBefore(new CustomFilter(), UsernamePasswordAuthenticationFilter.class)
            .csrf().disable() // Désactiver CSRF pour simplifier l'exemple
            .authorizeRequests()
                .antMatchers("/public/**").permitAll() // Autoriser l'accès public
                .anyRequest().authenticated() // Toutes les autres requêtes nécessitent une authentification
            .and()
            .formLogin() // Configuration du formulaire de connexion
                .loginPage("/login")
                .permitAll()
            .and()
            .logout()
                .permitAll();
    }

    @Bean
    public CustomFilter customFilter() {
        return new CustomFilter();
    }
}
```

**Le filtre CustomFilter**

mentionné dans la configuration est un exemple de filtre personnalisé que vous pouvez implémenter pour effectuer des vérifications de sécurité spécifiques à votre application. Voici comment vous pourriez le créer :

```java
import javax.servlet.Filter;
import javax.servlet.FilterChain;
import javax.servlet.FilterConfig;
import javax.servlet.ServletException;
import javax.servlet.ServletRequest;
import javax.servlet.ServletResponse;
import java.io.IOException;

public class CustomFilter implements Filter {

    @Override
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain)
            throws IOException, ServletException {
        // Vos vérifications de sécurité personnalisées ici
        // Par exemple, validation des paramètres de requête, protection contre les attaques, etc.

        // Passez la requête à la chaîne de filtres suivante
        chain.doFilter(request, response);
    }

    @Override
    public void init(FilterConfig filterConfig) throws ServletException {
        // Initialisation du filtre
    }
```

## Un exemple de CustomFilter qui inclut quelques protections de sécurité de base :

```java
import javax.servlet.Filter;
import javax.servlet.FilterChain;
import javax.servlet.FilterConfig;
import javax.servlet.ServletException;
import javax.servlet.ServletRequest;
import javax.servlet.ServletResponse;
import java.io.IOException;
import java.util.regex.Pattern;

public class CustomFilter implements Filter {

    @Override
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain)
            throws IOException, ServletException {
        // Protection contre les attaques XSS (Cross-Site Scripting)
        String paramValue = request.getParameter("param");
        if (paramValue != null && containsScript(paramValue)) {
            throw new ServletException("Blocked by WAF: Cross-Site Scripting (XSS) attack detected");
        }

        // Protection contre les attaques d'injection SQL
        String sqlParamValue = request.getParameter("sqlParam");
        if (sqlParamValue != null && containsSQL(sqlParamValue)) {
            throw new ServletException("Blocked by WAF: SQL Injection attack detected");
        }

        // Vos vérifications de sécurité personnalisées ici

        // Passez la requête à la chaîne de filtres suivante
        chain.doFilter(request, response);
    }

    private boolean containsScript(String value) {
        // Vérifie si la valeur contient des balises de script potentiellement malveillantes
        return Pattern.compile("<script>", Pattern.CASE_INSENSITIVE).matcher(value).find();
    }

    private boolean containsSQL(String value) {
        // Vérifie si la valeur contient des chaînes SQL potentiellement malveillantes
        return Pattern.compile("\\b(?:select|insert|update|delete)\\b", Pattern.CASE_INSENSITIVE).matcher(value).find();
    }

    @Override
    public void init(FilterConfig filterConfig) throws ServletException {
        // Initialisation du filtre
    }

    @Override
    public void destroy() {
        // Libération des ressources lors de la destruction du filtre
    }
}
```

Dans cet exemple, le filtre effectue deux vérifications de sécurité basiques : une pour détecter les attaques XSS (Cross-Site Scripting) et une pour détecter les attaques d'injection SQL. Vous devrez étendre ce filtre en fonction des besoins spécifiques de votre application et des types d'attaques que vous souhaitez protéger contre elles.
