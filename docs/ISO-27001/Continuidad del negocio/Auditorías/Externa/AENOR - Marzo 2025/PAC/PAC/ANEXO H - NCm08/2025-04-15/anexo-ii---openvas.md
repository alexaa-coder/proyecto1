April 14, 2025

## Report


Prepared By

###### HostedScan Security


[hostedscan.com](https://hostedscan.com/?utm_source=report)





![](/img/anexo-ii---openvas/Anexo-II---OpenVAS.pdf-0-0.png)
HostedScan Security Vulnerability Scan Report



&gt; Table omitted (Table 2): duplicated data detected.
&gt; Source document: Anexo II - OpenVAS.pdf




[hostedscan.com](https://hostedscan.com/?utm_source=report)



2



![](/img/anexo-ii---openvas/Anexo-II---OpenVAS.pdf-1-0.png)
Executive Summary Vulnerability Scan Report

#### Executive Summary


Vulnerability scans were conducted on select servers, networks, websites, and applications. This report contains the


discovered potential vulnerabilities from these scans. Vulnerabilities have been classified by severity. Higher severity


indicates a greater risk of a data breach, loss of integrity, or availability of the targets.

###### Total Vulnerabilities


Below are the total number of vulnerabilities found by severity. Critical vulnerabilities are the most severe and should


be evaluated first. An accepted vulnerability is one which has been manually reviewed and classified as acceptable


to not fix at this time, such as a false positive detection or an intentional part of the system's architecture.



![](/img/anexo-ii---openvas/Anexo-II---OpenVAS.pdf-2-0.png)



![](/img/anexo-ii---openvas/Anexo-II---OpenVAS.pdf-2-1.png)



![](/img/anexo-ii---openvas/Anexo-II---OpenVAS.pdf-2-2.png)



![](/img/anexo-ii---openvas/Anexo-II---OpenVAS.pdf-2-3.png)



![](/img/anexo-ii---openvas/Anexo-II---OpenVAS.pdf-2-4.png)



5% 11% 81% 3%

###### Report Coverage


This report includes findings for 1 target scanned. Each target is a single URL, IP address, or fully qualified domain


name (FQDN).


Vulnerability Categories

### 37

Network Vulnerabilities



[hostedscan.com](https://hostedscan.com/?utm_source=report)



3


Vulnerabilities By Target Vulnerability Scan Report

#### Vulnerabilities By Target


This section contains the vulnerability findings for each scanned target. Prioritization should be given to the


targets with the highest severity vulnerabilities. However, it is important to take into account the purpose of each


system and consider the potential impact a breach or an outage would have for the particular target.

###### Targets Summary


The number of potential vulnerabilities found for each target by severity.



![](/img/anexo-ii---openvas/Anexo-II---OpenVAS.pdf-3-0.png)



[hostedscan.com](https://hostedscan.com/?utm_source=report)



4


Vulnerabilities By Target | spikatech.com Vulnerability Scan Report

###### Target Breakdowns


Details for the potential vulnerabilities found for each target by scan type.

#### spikatech.com


Total Risks


5% 11% 81% 3%



![](/img/anexo-ii---openvas/Anexo-II---OpenVAS.pdf-4-5.png)











[hostedscan.com](https://hostedscan.com/?utm_source=report)



5


Vulnerabilities By Target | spikatech.com Vulnerability Scan Report



![](/img/anexo-ii---openvas/Anexo-II---OpenVAS.pdf-5-0.png)







[hostedscan.com](https://hostedscan.com/?utm_source=report)



6


Vulnerabilities By Target | spikatech.com Vulnerability Scan Report



![](/img/anexo-ii---openvas/Anexo-II---OpenVAS.pdf-6-0.png)







[hostedscan.com](https://hostedscan.com/?utm_source=report)



7


Network Vulnerabilities Vulnerability Scan Report

#### Network Vulnerabilities


The OpenVAS network vulnerability scan tests servers and internet connected devices for over 150,000


vulnerabilities. OpenVAS uses the Common Vulnerability Scoring System (CVSS) to quantify the severity of findings.


0.0 is the lowest severity and 10.0 is the highest.


Lite Scan


Free accounts use the lite network scan which is limited to the 10 most common ports and excludes brute


force tests.

###### Total Vulnerabilities


Total number of vulnerabilities found by severity.



![](/img/anexo-ii---openvas/Anexo-II---OpenVAS.pdf-7-0.png)





![](/img/anexo-ii---openvas/Anexo-II---OpenVAS.pdf-7-1.png)



![](/img/anexo-ii---openvas/Anexo-II---OpenVAS.pdf-7-2.png)



![](/img/anexo-ii---openvas/Anexo-II---OpenVAS.pdf-7-3.png)



![](/img/anexo-ii---openvas/Anexo-II---OpenVAS.pdf-7-4.png)



5% 11% 81% 3%

###### Vulnerabilities Breakdown


Summary list of all detected vulnerabilities.



![](/img/anexo-ii---openvas/Anexo-II---OpenVAS.pdf-7-5.png)



[hostedscan.com](https://hostedscan.com/?utm_source=report)



8


Network Vulnerabilities Vulnerability Scan Report



![](/img/anexo-ii---openvas/Anexo-II---OpenVAS.pdf-8-0.png)

















[hostedscan.com](https://hostedscan.com/?utm_source=report)



9


Network Vulnerabilities Vulnerability Scan Report



![](/img/anexo-ii---openvas/Anexo-II---OpenVAS.pdf-9-0.png)









[hostedscan.com](https://hostedscan.com/?utm_source=report)



10


Network Vulnerabilities | Missing 'HttpOnly' Cookie Attribute (HTTP) Vulnerability Scan Report

###### Vulnerability Details


Detailed information about each potential vulnerability found by the scan.

#### Missing 'HttpOnly' Cookie Attribute (HTTP)



LAST DETECTED

0 days ago



CVSS SCORE

5.0



SEVERITY

Medium



AFFECTED TARGETS

1 target



Description
The remote HTTP web server / application is missing to set the 'HttpOnly' cookie attribute for one or more sent HTTP cookie.


The flaw exists if a session cookie is not using the 'HttpOnly' cookie attribute.


This allows a cookie to be accessed by JavaScript which could lead to session hijacking attacks.


Solution

- Set the 'HttpOnly' cookie attribute for any session cookie


- Evaluate / do an own assessment of the security impact on the web server / application and create an override for this result if there is
none (this can't be checked automatically by this VT)


References

[https://www.rfc-editor.org/rfc/rfc6265#section-5.2.6](https://www.rfc-editor.org/rfc/rfc6265#section-5.2.6)
[https://owasp.org/www-community/HttpOnly](https://owasp.org/www-community/HttpOnly)
[https://wiki.owasp.org/index.php/Testing_for_cookies_attributes_(OTG-SESS-002)](https://wiki.owasp.org/index.php/Testing_for_cookies_attributes_(OTG-SESS-002))



![](/img/anexo-ii---openvas/Anexo-II---OpenVAS.pdf-10-0.png)



[hostedscan.com](https://hostedscan.com/?utm_source=report)



11


Network Vulnerabilities | Missing 'HttpOnly' Cookie Attribute (HTTP) Vulnerability Scan Report

#### Missing 'HttpOnly' Cookie Attribute (HTTP)



LAST DETECTED

0 days ago



CVSS SCORE

5.0



SEVERITY

Medium



AFFECTED TARGETS

1 target



Description
The remote HTTP web server / application is missing to set the 'HttpOnly' cookie attribute for one or more sent HTTP cookie.


The flaw exists if a session cookie is not using the 'HttpOnly' cookie attribute.


This allows a cookie to be accessed by JavaScript which could lead to session hijacking attacks.


Solution

- Set the 'HttpOnly' cookie attribute for any session cookie


- Evaluate / do an own assessment of the security impact on the web server / application and create an override for this result if there is
none (this can't be checked automatically by this VT)


References

[https://www.rfc-editor.org/rfc/rfc6265#section-5.2.6](https://www.rfc-editor.org/rfc/rfc6265#section-5.2.6)
[https://owasp.org/www-community/HttpOnly](https://owasp.org/www-community/HttpOnly)



&gt; Table omitted (Table 3): duplicated data detected.
&gt; Source document: Anexo II - OpenVAS.pdf




[hostedscan.com](https://hostedscan.com/?utm_source=report)



12


Network Vulnerabilities | WordPress Contact Form 7 Plugin &lt; 5.3.2 RCE Vulnerability Vulnerability Scan Report

#### WordPress Contact Form 7 Plugin &lt; 5.3.2 RCE Vulnerability



LAST DETECTED

0 days ago



CVSS SCORE

10.0



SEVERITY

Critical



AFFECTED TARGETS

1 target



Description
The WordPress plugin 'Contact Form 7' is prone to an unrestricted file upload and remote code execution (RCE) vulnerability because a
filename may contain special characters.


Attackers may upload files of any type, bypassing all restrictions placed regarding the allowed upload-able file types on a website.
Further, it allows an attacker to inject malicious content such as web shells.


Solution
Update to version 5.3.2 or later.


References

CVE-2020-35489
[https://contactform7.com/2020/12/17/contact-form-7-532/](https://contactform7.com/2020/12/17/contact-form-7-532/)
[https://www.getastra.com/blog/911/plugin-exploit/contact-form-7-unrestricted-file-upload/](https://www.getastra.com/blog/911/plugin-exploit/contact-form-7-unrestricted-file-upload/)
[https://www.jinsonvarghese.com/unrestricted-file-upload-in-contact-form-7/](https://www.jinsonvarghese.com/unrestricted-file-upload-in-contact-form-7/)



![](/img/anexo-ii---openvas/Anexo-II---OpenVAS.pdf-12-0.png)



[hostedscan.com](https://hostedscan.com/?utm_source=report)



13


Network Vulnerabilities | WordPress Contact Form 7 Plugin &lt; 5.3.2 RCE Vulnerability Vulnerability Scan Report

#### WordPress Contact Form 7 Plugin &lt; 5.3.2 RCE Vulnerability



LAST DETECTED

0 days ago



CVSS SCORE

10.0



SEVERITY

Critical



AFFECTED TARGETS

1 target



Description
The WordPress plugin 'Contact Form 7' is prone to an unrestricted file upload and remote code execution (RCE) vulnerability because a
filename may contain special characters.


Attackers may upload files of any type, bypassing all restrictions placed regarding the allowed upload-able file types on a website.
Further, it allows an attacker to inject malicious content such as web shells.


Solution
Update to version 5.3.2 or later.


References

CVE-2020-35489
[https://contactform7.com/2020/12/17/contact-form-7-532/](https://contactform7.com/2020/12/17/contact-form-7-532/)
[https://www.getastra.com/blog/911/plugin-exploit/contact-form-7-unrestricted-file-upload/](https://www.getastra.com/blog/911/plugin-exploit/contact-form-7-unrestricted-file-upload/)
[https://www.jinsonvarghese.com/unrestricted-file-upload-in-contact-form-7/](https://www.jinsonvarghese.com/unrestricted-file-upload-in-contact-form-7/)



![](/img/anexo-ii---openvas/Anexo-II---OpenVAS.pdf-13-0.png)



[hostedscan.com](https://hostedscan.com/?utm_source=report)



14


Network Vulnerabilities | WordPress Shortcodes Ultimate Plugin &lt; 5.12.1 Multiple CSRF Vulnerabilities Vulnerability Scan Report

#### WordPress Shortcodes Ultimate Plugin &lt; 5.12.1 Multiple CSRF Vulnerabilities



LAST DETECTED

0 days ago



CVSS SCORE

8.8



SEVERITY

High



AFFECTED TARGETS

1 target



Description
The WordPress plugin 'Shortcodes Ultimate' is prone to multiple cross-site request forgery (CSRF) vulnerabilities.


The following vulnerabilities exist:


- CVE-2022-38086: Cross-Site Request Forgery (CSRF) vulnerability leading to plugin preset settings change.


- CVE-2022-41136: Cross-Site Request Forgery (CSRF) vulnerability leading to Stored Cross-Site Scripting (XSS).


Solution
Update to version 5.12.1 or later.


References

CVE-2022-38086
CVE-2022-41136
https://patchstack.com/database/vulnerability/shortcodes-ultimate/wordpress-shortcodes-ultimate-plugin-5-12-0-cross-site-request-forgery-csrfvulnerability?_s_id=cve
https://patchstack.com/database/vulnerability/shortcodes-ultimate/wordpress-shortcodes-ultimate-plugin-5-12-0-csrf-vulnerability-leading-tostored-xss?_s_id=cve



![](/img/anexo-ii---openvas/Anexo-II---OpenVAS.pdf-14-0.png)

[hostedscan.com](https://hostedscan.com/?utm_source=report)



15


Network Vulnerabilities | WordPress Shortcodes Ultimate Plugin &lt; 5.12.1 Multiple CSRF Vulnerabilities Vulnerability Scan Report

#### WordPress Shortcodes Ultimate Plugin &lt; 5.12.1 Multiple CSRF Vulnerabilities



LAST DETECTED

0 days ago



CVSS SCORE

8.8



SEVERITY

High



AFFECTED TARGETS

1 target



Description
The WordPress plugin 'Shortcodes Ultimate' is prone to multiple cross-site request forgery (CSRF) vulnerabilities.


The following vulnerabilities exist:


- CVE-2022-38086: Cross-Site Request Forgery (CSRF) vulnerability leading to plugin preset settings change.


- CVE-2022-41136: Cross-Site Request Forgery (CSRF) vulnerability leading to Stored Cross-Site Scripting (XSS).


Solution
Update to version 5.12.1 or later.


References

CVE-2022-38086
CVE-2022-41136
https://patchstack.com/database/vulnerability/shortcodes-ultimate/wordpress-shortcodes-ultimate-plugin-5-12-0-cross-site-request-forgery-csrfvulnerability?_s_id=cve
https://patchstack.com/database/vulnerability/shortcodes-ultimate/wordpress-shortcodes-ultimate-plugin-5-12-0-csrf-vulnerability-leading-tostored-xss?_s_id=cve



![](/img/anexo-ii---openvas/Anexo-II---OpenVAS.pdf-15-0.png)



[hostedscan.com](https://hostedscan.com/?utm_source=report)



16


Network Vulnerabilities | WordPress Popup Maker Plugin &lt; 1.18.0 Information Disclosure Vulnerability Vulnerability Scan Report

#### WordPress Popup Maker Plugin &lt; 1.18.0 Information Disclosure Vulnerability



LAST DETECTED

0 days ago



CVSS SCORE

7.5



SEVERITY

High



AFFECTED TARGETS

1 target



Description
The WordPress plugin 'Popup Maker' is prone to an information disclosure vulnerability.


The plugin generates a predictable name when creating debug log files.


Unauthenticated attackers are able to view log files.


Solution
Update to version 1.18.0 or later.


References

CVE-2022-47597
[https://patchstack.com/database/vulnerability/popup-maker/wordpress-popup-maker-plugin-1-17-1-unauth-access-to-debug-log](https://patchstack.com/database/vulnerability/popup-maker/wordpress-popup-maker-plugin-1-17-1-unauth-access-to-debug-log)


[hostedscan.com](https://hostedscan.com/?utm_source=report)



![](/img/anexo-ii---openvas/Anexo-II---OpenVAS.pdf-16-0.png)

17


Network Vulnerabilities | WordPress Popup Maker Plugin &lt; 1.18.0 Information Disclosure Vulnerability Vulnerability Scan Report

#### WordPress Popup Maker Plugin &lt; 1.18.0 Information Disclosure Vulnerability



LAST DETECTED

0 days ago



CVSS SCORE

7.5



SEVERITY

High



AFFECTED TARGETS

1 target



Description
The WordPress plugin 'Popup Maker' is prone to an information disclosure vulnerability.


The plugin generates a predictable name when creating debug log files.


Unauthenticated attackers are able to view log files.


Solution
Update to version 1.18.0 or later.


References

CVE-2022-47597
[https://patchstack.com/database/vulnerability/popup-maker/wordpress-popup-maker-plugin-1-17-1-unauth-access-to-debug-log](https://patchstack.com/database/vulnerability/popup-maker/wordpress-popup-maker-plugin-1-17-1-unauth-access-to-debug-log)


[hostedscan.com](https://hostedscan.com/?utm_source=report)



![](/img/anexo-ii---openvas/Anexo-II---OpenVAS.pdf-17-0.png)

18


Network Vulnerabilities | WordPress Shortcodes Ultimate Plugin &lt; 5.10.2 XSS Vulnerability Vulnerability Scan Report

#### WordPress Shortcodes Ultimate Plugin &lt; 5.10.2 XSS Vulnerability



LAST DETECTED

0 days ago



CVSS SCORE

5.4



SEVERITY

Medium



AFFECTED TARGETS

1 target



Description
The WordPress plugin 'Shortcodes Ultimate' is prone to a cross-site scripting (XSS) vulnerability.


The plugin allows users with Contributor roles to perform stored XSS via shortcode attributes.


Note: the plugin is inconsistent in its handling of shortcode attributes. Some do escape, most don't, and there are even some attributes
that are insecure by design (like [su_button]'s onclick attribute).


Solution
Update to version 5.10.2 or later.


References

CVE-2021-24525
[https://wpscan.com/vulnerability/7f5659bd-50c3-4725-95f4-cf88812acf1c](https://wpscan.com/vulnerability/7f5659bd-50c3-4725-95f4-cf88812acf1c)
[https://plugins.trac.wordpress.org/browser/shortcodes-ultimate/trunk/changelog.txt](https://plugins.trac.wordpress.org/browser/shortcodes-ultimate/trunk/changelog.txt)



![](/img/anexo-ii---openvas/Anexo-II---OpenVAS.pdf-18-0.png)



[hostedscan.com](https://hostedscan.com/?utm_source=report)



19


Network Vulnerabilities | WordPress Shortcodes Ultimate Plugin &lt; 5.10.2 XSS Vulnerability Vulnerability Scan Report

#### WordPress Shortcodes Ultimate Plugin &lt; 5.10.2 XSS Vulnerability



LAST DETECTED

0 days ago



CVSS SCORE

5.4



SEVERITY

Medium



AFFECTED TARGETS

1 target



Description
The WordPress plugin 'Shortcodes Ultimate' is prone to a cross-site scripting (XSS) vulnerability.


The plugin allows users with Contributor roles to perform stored XSS via shortcode attributes.


Note: the plugin is inconsistent in its handling of shortcode attributes. Some do escape, most don't, and there are even some attributes
that are insecure by design (like [su_button]'s onclick attribute).


Solution
Update to version 5.10.2 or later.


References

CVE-2021-24525
[https://wpscan.com/vulnerability/7f5659bd-50c3-4725-95f4-cf88812acf1c](https://wpscan.com/vulnerability/7f5659bd-50c3-4725-95f4-cf88812acf1c)
[https://plugins.trac.wordpress.org/browser/shortcodes-ultimate/trunk/changelog.txt](https://plugins.trac.wordpress.org/browser/shortcodes-ultimate/trunk/changelog.txt)



![](/img/anexo-ii---openvas/Anexo-II---OpenVAS.pdf-19-0.png)



[hostedscan.com](https://hostedscan.com/?utm_source=report)



20


Network Vulnerabilities | WordPress Popup Maker Plugin &lt; 1.16.5 XSS Vulnerability Vulnerability Scan Report

#### WordPress Popup Maker Plugin &lt; 1.16.5 XSS Vulnerability



LAST DETECTED

0 days ago



CVSS SCORE

4.8



SEVERITY

Medium



AFFECTED TARGETS

1 target



Description
The WordPress plugin 'Popup Maker' is prone to a cross-site scripting (XSS) vulnerability.


The plugin does not sanitise and escape some of its Popup settings, which could allow high privilege users such as admin to perform
stored cross-site scripting attacks even when the unfiltered_html capability is disallowed.


Solution
Update to version 1.16.5 or later.


References

CVE-2022-1104
[https://wpscan.com/vulnerability/4d4709f3-ad38-4519-a24a-73bc04b20e52](https://wpscan.com/vulnerability/4d4709f3-ad38-4519-a24a-73bc04b20e52)



![](/img/anexo-ii---openvas/Anexo-II---OpenVAS.pdf-20-0.png)



[hostedscan.com](https://hostedscan.com/?utm_source=report)



21


Network Vulnerabilities | WordPress Popup Maker Plugin &lt; 1.16.9 Multiple XSS Vulnerabilities Vulnerability Scan Report

#### WordPress Popup Maker Plugin &lt; 1.16.9 Multiple XSS Vulnerabilities



LAST DETECTED

0 days ago



CVSS SCORE

5.4



SEVERITY

Medium



AFFECTED TARGETS

1 target



Description
The WordPress plugin 'Popup Maker' is prone to multiple cross-site scripting (XSS) vulnerabilities.


The plugin does not validate and escape one of its shortcode attributes, which could allow users with a role as low as contributor to
perform stored cross-site scripting attacks.


Solution
Update to version 1.16.9 or later.


References

CVE-2022-4362
CVE-2022-4381
[https://wpscan.com/vulnerability/2660225a-e4c8-40f2-8c98-775ef2301212](https://wpscan.com/vulnerability/2660225a-e4c8-40f2-8c98-775ef2301212)
[https://wpscan.com/vulnerability/8bf8ebe8-1063-492d-a0f9-2f824408d0df](https://wpscan.com/vulnerability/8bf8ebe8-1063-492d-a0f9-2f824408d0df)


[hostedscan.com](https://hostedscan.com/?utm_source=report)



![](/img/anexo-ii---openvas/Anexo-II---OpenVAS.pdf-21-0.png)

22


Network Vulnerabilities | WordPress Popup Maker Plugin &lt; 1.16.11 XSS Vulnerability Vulnerability Scan Report

#### WordPress Popup Maker Plugin &lt; 1.16.11 XSS Vulnerability



LAST DETECTED

0 days ago



CVSS SCORE

4.8



SEVERITY

Medium



AFFECTED TARGETS

1 target



Description
The WordPress plugin 'Popup Maker' is prone to a cross-site scripting (XSS) vulnerability.


The plugin does not sanitise and escape some of its Popup options, which could allow users with a role as low as Contributor to perform
stored cross-site scripting attacks, which could be used against admins.


Solution
Update to version 1.16.11 or later.


References

CVE-2022-3690
[https://wpscan.com/vulnerability/725f6ae4-7ec5-4d7c-9533-c9b61b59cc2b](https://wpscan.com/vulnerability/725f6ae4-7ec5-4d7c-9533-c9b61b59cc2b)



![](/img/anexo-ii---openvas/Anexo-II---OpenVAS.pdf-22-0.png)



[hostedscan.com](https://hostedscan.com/?utm_source=report)



23


Network Vulnerabilities | WordPress Popup Maker Plugin &lt; 1.16.5 XSS Vulnerability Vulnerability Scan Report

#### WordPress Popup Maker Plugin &lt; 1.16.5 XSS Vulnerability



LAST DETECTED

0 days ago



CVSS SCORE

4.8



SEVERITY

Medium



AFFECTED TARGETS

1 target



Description
The WordPress plugin 'Popup Maker' is prone to a cross-site scripting (XSS) vulnerability.


The plugin does not sanitise and escape some of its Popup settings, which could allow high privilege users such as admin to perform
stored cross-site scripting attacks even when the unfiltered_html capability is disallowed.


Solution
Update to version 1.16.5 or later.


References

CVE-2022-1104
[https://wpscan.com/vulnerability/4d4709f3-ad38-4519-a24a-73bc04b20e52](https://wpscan.com/vulnerability/4d4709f3-ad38-4519-a24a-73bc04b20e52)



![](/img/anexo-ii---openvas/Anexo-II---OpenVAS.pdf-23-0.png)



[hostedscan.com](https://hostedscan.com/?utm_source=report)



24


Network Vulnerabilities | WordPress Popup Maker Plugin &lt; 1.16.11 XSS Vulnerability Vulnerability Scan Report

#### WordPress Popup Maker Plugin &lt; 1.16.11 XSS Vulnerability



LAST DETECTED

0 days ago



CVSS SCORE

4.8



SEVERITY

Medium



AFFECTED TARGETS

1 target



Description
The WordPress plugin 'Popup Maker' is prone to a cross-site scripting (XSS) vulnerability.


The plugin does not sanitise and escape some of its Popup options, which could allow users with a role as low as Contributor to perform
stored cross-site scripting attacks, which could be used against admins.


Solution
Update to version 1.16.11 or later.


References

CVE-2022-3690
[https://wpscan.com/vulnerability/725f6ae4-7ec5-4d7c-9533-c9b61b59cc2b](https://wpscan.com/vulnerability/725f6ae4-7ec5-4d7c-9533-c9b61b59cc2b)



![](/img/anexo-ii---openvas/Anexo-II---OpenVAS.pdf-24-0.png)



[hostedscan.com](https://hostedscan.com/?utm_source=report)



25


Network Vulnerabilities | WordPress Popup Maker Plugin &lt; 1.16.9 Multiple XSS Vulnerabilities Vulnerability Scan Report

#### WordPress Popup Maker Plugin &lt; 1.16.9 Multiple XSS Vulnerabilities



LAST DETECTED

0 days ago



CVSS SCORE

5.4



SEVERITY

Medium



AFFECTED TARGETS

1 target



Description
The WordPress plugin 'Popup Maker' is prone to multiple cross-site scripting (XSS) vulnerabilities.


The plugin does not validate and escape one of its shortcode attributes, which could allow users with a role as low as contributor to
perform stored cross-site scripting attacks.


Solution
Update to version 1.16.9 or later.


References

CVE-2022-4362
CVE-2022-4381
[https://wpscan.com/vulnerability/2660225a-e4c8-40f2-8c98-775ef2301212](https://wpscan.com/vulnerability/2660225a-e4c8-40f2-8c98-775ef2301212)
[https://wpscan.com/vulnerability/8bf8ebe8-1063-492d-a0f9-2f824408d0df](https://wpscan.com/vulnerability/8bf8ebe8-1063-492d-a0f9-2f824408d0df)


[hostedscan.com](https://hostedscan.com/?utm_source=report)



![](/img/anexo-ii---openvas/Anexo-II---OpenVAS.pdf-25-0.png)

26


Network Vulnerabilities | WordPress Shortcodes Ultimate Plugin &lt; 5.12.8 Multiple Information Disclosure vulnerabilities Vulnerability Scan

#### WordPress Shortcodes Ultimate Plugin &lt; 5.12.8 Multiple Information Disclosure vulnerabilities



LAST DETECTED

0 days ago



CVSS SCORE

6.5



SEVERITY

Medium



AFFECTED TARGETS

1 target



Description
The WordPress plugin 'Shortcodes Ultimate' is prone to multiple information disclosure vulnerabilities.


The following vulnerabilities exist:


- CVE-2023-0890: The plugin does not ensure that posts to be displayed via some shortcodes are already public and can be accessed
by the user making the request, allowing any authenticated users such as subscriber to view draft, private or even password protected
posts. It is also possible to leak the password of protected posts.


- CVE-2023-0911: The plugin does not validate the user meta to be retrieved via the user shortcode, allowing any authenticated users
such as subscriber to retrieve arbitrary user meta (except the user_pass), such as the user email and activation key by default.


Solution
Update to version 5.12.8 or later.


References

CVE-2023-0890
CVE-2023-0911
[https://wpscan.com/vulnerability/8a466f15-f112-4527-8b02-4544a8032671](https://wpscan.com/vulnerability/8a466f15-f112-4527-8b02-4544a8032671)
[https://wpscan.com/vulnerability/35404d16-7213-4293-ac0d-926bd6c17444](https://wpscan.com/vulnerability/35404d16-7213-4293-ac0d-926bd6c17444)



![](/img/anexo-ii---openvas/Anexo-II---OpenVAS.pdf-26-0.png)



[hostedscan.com](https://hostedscan.com/?utm_source=report)



27


Network Vulnerabilities | WordPress Shortcodes Ultimate Plugin &lt; 5.12.8 Multiple Information Disclosure vulnerabilities Vulnerability Scan

#### WordPress Shortcodes Ultimate Plugin &lt; 5.12.8 Multiple Information Disclosure vulnerabilities



LAST DETECTED

0 days ago



CVSS SCORE

6.5



SEVERITY

Medium



AFFECTED TARGETS

1 target



Description
The WordPress plugin 'Shortcodes Ultimate' is prone to multiple information disclosure vulnerabilities.


The following vulnerabilities exist:


- CVE-2023-0890: The plugin does not ensure that posts to be displayed via some shortcodes are already public and can be accessed
by the user making the request, allowing any authenticated users such as subscriber to view draft, private or even password protected
posts. It is also possible to leak the password of protected posts.


- CVE-2023-0911: The plugin does not validate the user meta to be retrieved via the user shortcode, allowing any authenticated users
such as subscriber to retrieve arbitrary user meta (except the user_pass), such as the user email and activation key by default.


Solution
Update to version 5.12.8 or later.


References

CVE-2023-0890
CVE-2023-0911
[https://wpscan.com/vulnerability/8a466f15-f112-4527-8b02-4544a8032671](https://wpscan.com/vulnerability/8a466f15-f112-4527-8b02-4544a8032671)
[https://wpscan.com/vulnerability/35404d16-7213-4293-ac0d-926bd6c17444](https://wpscan.com/vulnerability/35404d16-7213-4293-ac0d-926bd6c17444)



![](/img/anexo-ii---openvas/Anexo-II---OpenVAS.pdf-27-0.png)



[hostedscan.com](https://hostedscan.com/?utm_source=report)



28


Network Vulnerabilities | WordPress ExactMetrics Plugin &lt; 7.12.1 XSS Vulnerability Vulnerability Scan Report

#### WordPress ExactMetrics Plugin &lt; 7.12.1 XSS Vulnerability



LAST DETECTED

0 days ago



CVSS SCORE

5.4



SEVERITY

Medium



AFFECTED TARGETS

1 target



Description
The WordPress plugin 'ExactMetrics' is prone to a cross-site scripting (XSS) vulnerability.


The plugin does not validate and escape some of its block options before outputting them back in a page/post where the block is
embed, which could allow users with the contributor role and above to perform Stored Cross-Site Scripting attacks.


Solution
Update to version 7.12.1 or later.


References

CVE-2023-0082
[https://wpscan.com/vulnerability/e1ba5047-0c39-478f-89c7-b0bb638efdff](https://wpscan.com/vulnerability/e1ba5047-0c39-478f-89c7-b0bb638efdff)


[hostedscan.com](https://hostedscan.com/?utm_source=report)



![](/img/anexo-ii---openvas/Anexo-II---OpenVAS.pdf-28-0.png)

29


Network Vulnerabilities | WordPress ExactMetrics Plugin &lt; 7.12.1 XSS Vulnerability Vulnerability Scan Report

#### WordPress ExactMetrics Plugin &lt; 7.12.1 XSS Vulnerability



LAST DETECTED

0 days ago



CVSS SCORE

5.4



SEVERITY

Medium



AFFECTED TARGETS

1 target



Description
The WordPress plugin 'ExactMetrics' is prone to a cross-site scripting (XSS) vulnerability.


The plugin does not validate and escape some of its block options before outputting them back in a page/post where the block is
embed, which could allow users with the contributor role and above to perform Stored Cross-Site Scripting attacks.


Solution
Update to version 7.12.1 or later.


References

CVE-2023-0082
[https://wpscan.com/vulnerability/e1ba5047-0c39-478f-89c7-b0bb638efdff](https://wpscan.com/vulnerability/e1ba5047-0c39-478f-89c7-b0bb638efdff)


[hostedscan.com](https://hostedscan.com/?utm_source=report)



![](/img/anexo-ii---openvas/Anexo-II---OpenVAS.pdf-29-0.png)

30


Network Vulnerabilities | WordPress MC4WP Plugin &lt; 4.8.7 XSS Vulnerability Vulnerability Scan Report

#### WordPress MC4WP Plugin &lt; 4.8.7 XSS Vulnerability



LAST DETECTED

0 days ago



CVSS SCORE

4.8



SEVERITY

Medium



AFFECTED TARGETS

1 target



Description
The WordPress plugin 'MC4WP' is prone to a cross-site scripting (XSS) vulnerability.


The plugin does not properly sanitise form data, which could allow high privilege users to perform cross-site scripting (XSS) attacks
when unfiltered_html is disallowed.


Solution
Update to version 4.8.7 or later.


References

CVE-2021-36833
[https://wpscan.com/vulnerability/da04b514-a561-4d25-95b8-1c7b5597f093](https://wpscan.com/vulnerability/da04b514-a561-4d25-95b8-1c7b5597f093)


[hostedscan.com](https://hostedscan.com/?utm_source=report)



![](/img/anexo-ii---openvas/Anexo-II---OpenVAS.pdf-30-0.png)

31


Network Vulnerabilities | WordPress MC4WP Plugin &lt; 4.8.7 XSS Vulnerability Vulnerability Scan Report

#### WordPress MC4WP Plugin &lt; 4.8.7 XSS Vulnerability



LAST DETECTED

0 days ago



CVSS SCORE

4.8



SEVERITY

Medium



AFFECTED TARGETS

1 target



Description
The WordPress plugin 'MC4WP' is prone to a cross-site scripting (XSS) vulnerability.


The plugin does not properly sanitise form data, which could allow high privilege users to perform cross-site scripting (XSS) attacks
when unfiltered_html is disallowed.


Solution
Update to version 4.8.7 or later.


References

CVE-2021-36833
[https://wpscan.com/vulnerability/da04b514-a561-4d25-95b8-1c7b5597f093](https://wpscan.com/vulnerability/da04b514-a561-4d25-95b8-1c7b5597f093)


[hostedscan.com](https://hostedscan.com/?utm_source=report)



![](/img/anexo-ii---openvas/Anexo-II---OpenVAS.pdf-31-0.png)

32


Network Vulnerabilities | WordPress ExactMetrics Plugin &lt; 7.14.2 XSS Vulnerability Vulnerability Scan Report

#### WordPress ExactMetrics Plugin &lt; 7.14.2 XSS Vulnerability



LAST DETECTED

0 days ago



CVSS SCORE

5.4



SEVERITY

Medium



AFFECTED TARGETS

1 target



Description
The WordPress plugin 'ExactMetrics' is prone to a cross-site scripting (XSS) vulnerability.


This could allow a malicious actor to inject malicious scripts, such as redirects, advertisements, and other HTML payloads into your
website which will be executed when guests visit your site.


Solution
Update to version 7.14.2 or later.


References

CVE-2023-23880
https://patchstack.com/database/vulnerability/google-analytics-dashboard-for-wp/wordpress-exactmetrics-plugin-7-14-1-cross-site-scripting-xssvulnerability



![](/img/anexo-ii---openvas/Anexo-II---OpenVAS.pdf-32-0.png)



[hostedscan.com](https://hostedscan.com/?utm_source=report)



33


Network Vulnerabilities | WordPress ExactMetrics Plugin &lt; 7.14.2 XSS Vulnerability Vulnerability Scan Report

#### WordPress ExactMetrics Plugin &lt; 7.14.2 XSS Vulnerability



LAST DETECTED

0 days ago



CVSS SCORE

5.4



SEVERITY

Medium



AFFECTED TARGETS

1 target



Description
The WordPress plugin 'ExactMetrics' is prone to a cross-site scripting (XSS) vulnerability.


This could allow a malicious actor to inject malicious scripts, such as redirects, advertisements, and other HTML payloads into your
website which will be executed when guests visit your site.


Solution
Update to version 7.14.2 or later.


References

CVE-2023-23880
https://patchstack.com/database/vulnerability/google-analytics-dashboard-for-wp/wordpress-exactmetrics-plugin-7-14-1-cross-site-scripting-xssvulnerability



![](/img/anexo-ii---openvas/Anexo-II---OpenVAS.pdf-33-0.png)



[hostedscan.com](https://hostedscan.com/?utm_source=report)



34


Network Vulnerabilities | WordPress Shortcodes Ultimate Plugin &lt; 7.0.0 Multiple Vulnerabilities Vulnerability Scan Report

#### WordPress Shortcodes Ultimate Plugin &lt; 7.0.0 Multiple Vulnerabilities



LAST DETECTED

0 days ago



CVSS SCORE

5.4



SEVERITY

Medium



AFFECTED TARGETS

1 target



Description
The WordPress plugin 'Shortcodes Ultimate' is prone to multiple vulnerabilities.


The following vulnerabilities exist:


- CVE-2023-6225: Authenticated attackers are able to inject arbitrary web scripts in pages that will execute whenever a user accesses
an injected page due to insufficient input sanitization and output escaping on user supplied meta values.


- CVE-2023-6226: Authenticated attackers are able to retrieve arbitrary post meta values which may contain sensitive information due
to missing validation on the user controlled keys 'key' and 'post_id' in the su_meta shortcode.


Solution
Update to version 7.0.0 or later.


References

CVE-2023-6225
CVE-2023-6226
[https://www.wordfence.com/threat-intel/vulnerabilities/id/558e36f6-4678-46a2-8154-42770fbb5574](https://www.wordfence.com/threat-intel/vulnerabilities/id/558e36f6-4678-46a2-8154-42770fbb5574)
[https://www.wordfence.com/threat-intel/vulnerabilities/id/4d936a48-b300-4a41-8d28-ba34cb3c5cb7](https://www.wordfence.com/threat-intel/vulnerabilities/id/4d936a48-b300-4a41-8d28-ba34cb3c5cb7)



![](/img/anexo-ii---openvas/Anexo-II---OpenVAS.pdf-34-0.png)



[hostedscan.com](https://hostedscan.com/?utm_source=report)



35


Network Vulnerabilities Vulnerability Scan Report

#### WordPress Shortcodes Ultimate Plugin &lt; 7.0.0 Multiple Vulnerabilities



LAST DETECTED

0 days ago



CVSS SCORE

5.4



SEVERITY

Medium



AFFECTED TARGETS

1 target



Description
The WordPress plugin 'Shortcodes Ultimate' is prone to multiple vulnerabilities.


The following vulnerabilities exist:


- CVE-2023-6225: Authenticated attackers are able to inject arbitrary web scripts in pages that will execute whenever a user accesses
an injected page due to insufficient input sanitization and output escaping on user supplied meta values.


- CVE-2023-6226: Authenticated attackers are able to retrieve arbitrary post meta values which may contain sensitive information due
to missing validation on the user controlled keys 'key' and 'post_id' in the su_meta shortcode.


Solution
Update to version 7.0.0 or later.


References

CVE-2023-6225
CVE-2023-6226
[https://www.wordfence.com/threat-intel/vulnerabilities/id/558e36f6-4678-46a2-8154-42770fbb5574](https://www.wordfence.com/threat-intel/vulnerabilities/id/558e36f6-4678-46a2-8154-42770fbb5574)
[https://www.wordfence.com/threat-intel/vulnerabilities/id/4d936a48-b300-4a41-8d28-ba34cb3c5cb7](https://www.wordfence.com/threat-intel/vulnerabilities/id/4d936a48-b300-4a41-8d28-ba34cb3c5cb7)



![](/img/anexo-ii---openvas/Anexo-II---OpenVAS.pdf-35-0.png)



[hostedscan.com](https://hostedscan.com/?utm_source=report)



36


Network Vulnerabilities | WordPress &lt; 6.5 Private Information Exposure Vulnerability Vulnerability Scan Report

#### WordPress &lt; 6.5 Private Information Exposure Vulnerability



LAST DETECTED

0 days ago



CVSS SCORE

5.3



SEVERITY

Medium



AFFECTED TARGETS

1 target



Description
WordPress is prone to a private information exposure via 'redirect_guess_404_permalink()'.


When guessing the proper URL to redirect a 404, WordPress only considers the post statuses and not the proper post type privacy
settings, leading to potential information disclosure.


This can allow unauthenticated attackers to expose the slug of a custom post whose 'publicly_queryable' post status has been set to
'false'.


Solution
Update to version 6.5 or later.


Note: As of 04/2024 the security fix is only available in version 6.5 and haven't been 'backported' to older versions yet.


References

CVE-2023-5692
[https://core.trac.wordpress.org/ticket/59795](https://core.trac.wordpress.org/ticket/59795)
[https://core.trac.wordpress.org/changeset/57645](https://core.trac.wordpress.org/changeset/57645)
[https://bugzilla.redhat.com/show_bug.cgi?id=2273662](https://bugzilla.redhat.com/show_bug.cgi?id=2273662)
[https://www.wordfence.com/threat-intel/vulnerabilities/id/6e6f993b-ce09-4050-84a1-cbe9953f36b1](https://www.wordfence.com/threat-intel/vulnerabilities/id/6e6f993b-ce09-4050-84a1-cbe9953f36b1)
https://patchstack.com/database/vulnerability/wordpress/wordpress-wordpress-core-plugin-6-4-3-sensitive-information-exposure-via-redirectguess-404-permalink-vulnerability


[hostedscan.com](https://hostedscan.com/?utm_source=report)



![](/img/anexo-ii---openvas/Anexo-II---OpenVAS.pdf-36-0.png)

37


Network Vulnerabilities | WordPress &lt; 6.5 Private Information Exposure Vulnerability Vulnerability Scan Report

#### WordPress &lt; 6.5 Private Information Exposure Vulnerability



LAST DETECTED

0 days ago



CVSS SCORE

5.3



SEVERITY

Medium



AFFECTED TARGETS

1 target



Description
WordPress is prone to a private information exposure via 'redirect_guess_404_permalink()'.


When guessing the proper URL to redirect a 404, WordPress only considers the post statuses and not the proper post type privacy
settings, leading to potential information disclosure.


This can allow unauthenticated attackers to expose the slug of a custom post whose 'publicly_queryable' post status has been set to
'false'.


Solution
Update to version 6.5 or later.


Note: As of 04/2024 the security fix is only available in version 6.5 and haven't been 'backported' to older versions yet.


References

CVE-2023-5692
[https://core.trac.wordpress.org/ticket/59795](https://core.trac.wordpress.org/ticket/59795)
[https://core.trac.wordpress.org/changeset/57645](https://core.trac.wordpress.org/changeset/57645)
[https://bugzilla.redhat.com/show_bug.cgi?id=2273662](https://bugzilla.redhat.com/show_bug.cgi?id=2273662)
[https://www.wordfence.com/threat-intel/vulnerabilities/id/6e6f993b-ce09-4050-84a1-cbe9953f36b1](https://www.wordfence.com/threat-intel/vulnerabilities/id/6e6f993b-ce09-4050-84a1-cbe9953f36b1)
https://patchstack.com/database/vulnerability/wordpress/wordpress-wordpress-core-plugin-6-4-3-sensitive-information-exposure-via-redirectguess-404-permalink-vulnerability


[hostedscan.com](https://hostedscan.com/?utm_source=report)



![](/img/anexo-ii---openvas/Anexo-II---OpenVAS.pdf-37-0.png)

38


Network Vulnerabilities | WordPress Popup Maker Plugin &lt; 1.18.3 XSS Vulnerability Vulnerability Scan Report

#### WordPress Popup Maker Plugin &lt; 1.18.3 XSS Vulnerability



LAST DETECTED

0 days ago



CVSS SCORE

5.4



SEVERITY

Medium



AFFECTED TARGETS

1 target



Description
The WordPress plugin 'Popup Maker' is prone to a cross-site scripting (XSS) vulnerability.


The WordPress 'Popup Maker' plugin allows cross-site scripting attacks due to insufficient input sanitization and output escaping on
user supplied attributes.


Attackers with contributor-level and above permissions are able to inject arbitrary web scripts in pages that will execute whenever a user
accesses an injected page.


Solution
Update to version 1.18.3 or later.


References

CVE-2024-2336
[https://wpscan.com/vulnerability/673562fe-e2be-407b-b6ef-b706f9ac769a](https://wpscan.com/vulnerability/673562fe-e2be-407b-b6ef-b706f9ac769a)



![](/img/anexo-ii---openvas/Anexo-II---OpenVAS.pdf-38-0.png)



[hostedscan.com](https://hostedscan.com/?utm_source=report)



39


Network Vulnerabilities | WordPress Popup Maker Plugin &lt; 1.18.3 XSS Vulnerability Vulnerability Scan Report

#### WordPress Popup Maker Plugin &lt; 1.18.3 XSS Vulnerability



LAST DETECTED

0 days ago



CVSS SCORE

5.4



SEVERITY

Medium



AFFECTED TARGETS

1 target



Description
The WordPress plugin 'Popup Maker' is prone to a cross-site scripting (XSS) vulnerability.


The WordPress 'Popup Maker' plugin allows cross-site scripting attacks due to insufficient input sanitization and output escaping on
user supplied attributes.


Attackers with contributor-level and above permissions are able to inject arbitrary web scripts in pages that will execute whenever a user
accesses an injected page.


Solution
Update to version 1.18.3 or later.


References

CVE-2024-2336
[https://wpscan.com/vulnerability/673562fe-e2be-407b-b6ef-b706f9ac769a](https://wpscan.com/vulnerability/673562fe-e2be-407b-b6ef-b706f9ac769a)



![](/img/anexo-ii---openvas/Anexo-II---OpenVAS.pdf-39-0.png)



[hostedscan.com](https://hostedscan.com/?utm_source=report)



40


Network Vulnerabilities | WordPress Shortcodes Ultimate Plugin &lt; 7.0.4 - Contributor+ Stored XSS Vulnerability Vulnerability Scan Report

#### WordPress Shortcodes Ultimate Plugin &lt; 7.0.4 - Contributor+ Stored XSS Vulnerability



LAST DETECTED

0 days ago



CVSS SCORE

5.4



SEVERITY

Medium



AFFECTED TARGETS

1 target



Description
The WordPress plugin 'Shortcodes Ultimate' is prone to a cross-site scripting (XSS) vulnerability.


The plugin is vulnerable to stored XSS via the plugin's 'su_qrcode' shortcode due to insufficient input sanitization and output escaping
on user supplied attributes.


Authenticated attackers with contributor-level access and above are able to inject arbitrary web scripts in pages that will execute
whenever a user accesses an injected page.


Solution
Update to version 7.0.4 or later.


References

CVE-2024-1808
https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/shortcodes-ultimate/wp-shortcodes-plugin-shortcodes-ultimate-703authenticated-contributor-stored-cross-site-scripting-via-su-qrcode-shortcode
[https://plugins.trac.wordpress.org/changeset/3041647/shortcodes-ultimate](https://plugins.trac.wordpress.org/changeset/3041647/shortcodes-ultimate)



![](/img/anexo-ii---openvas/Anexo-II---OpenVAS.pdf-40-0.png)



[hostedscan.com](https://hostedscan.com/?utm_source=report)



41


Network Vulnerabilities | WordPress Shortcodes Ultimate Plugin &lt; 7.0.5 - Contributor+ Stored XSS Vulnerability Vulnerability Scan Report

#### WordPress Shortcodes Ultimate Plugin &lt; 7.0.5 - Contributor+ Stored XSS Vulnerability



LAST DETECTED

0 days ago



CVSS SCORE

5.5



SEVERITY

Medium



AFFECTED TARGETS

1 target



Description
The WordPress plugin 'Shortcodes Ultimate' is prone to a cross-site scripting (XSS) vulnerability.


The plugin is vulnerable to stored XSS due to not properly escaping some of its shortcodes attributes before they are echoed back to
users.


Attackers with contributor-level permissions can conduct stored XSS attacks.


Solution
Update to version 7.0.5 or later.


References

CVE-2024-2583
[https://wpscan.com/vulnerability/98d8c713-e8cd-4fad-a8fb-7a40db2742a2/](https://wpscan.com/vulnerability/98d8c713-e8cd-4fad-a8fb-7a40db2742a2/)


[hostedscan.com](https://hostedscan.com/?utm_source=report)



![](/img/anexo-ii---openvas/Anexo-II---OpenVAS.pdf-41-0.png)

42


Network Vulnerabilities | WordPress Shortcodes Ultimate Plugin &lt; 7.1.3 - Contributor+ Stored XSS Vulnerability Vulnerability Scan Report

#### WordPress Shortcodes Ultimate Plugin &lt; 7.1.3 - Contributor+ Stored XSS Vulnerability



LAST DETECTED

0 days ago



CVSS SCORE

5.4



SEVERITY

Medium



AFFECTED TARGETS

1 target



Description
The WordPress plugin 'Shortcodes Ultimate' is prone to a cross-site scripting (XSS) vulnerability.


The plugin is vulnerable to stored XSS due to insufficient input sanitization and output escaping on user supplied attributes.


Authenticated attackers with contributor-level access and above are able to inject arbitrary web scripts in pages that will execute
whenever a user accesses an injected page.


Solution
Update to version 7.1.3 or later.


References

CVE-2024-3550
https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/shortcodes-ultimate/wp-shortcodes-plugin-shortcodes-ultimate-712authenticated-contributor-stored-cross-site-scripting-via-shortcode


[hostedscan.com](https://hostedscan.com/?utm_source=report)



![](/img/anexo-ii---openvas/Anexo-II---OpenVAS.pdf-42-0.png)

43


Network Vulnerabilities | WordPress Shortcodes Ultimate Plugin &lt; 7.0.4 - Contributor+ Stored XSS Vulnerability Vulnerability Scan Report

#### WordPress Shortcodes Ultimate Plugin &lt; 7.0.4 - Contributor+ Stored XSS Vulnerability



LAST DETECTED

0 days ago



CVSS SCORE

5.4



SEVERITY

Medium



AFFECTED TARGETS

1 target



Description
The WordPress plugin 'Shortcodes Ultimate' is prone to a cross-site scripting (XSS) vulnerability.


The plugin is vulnerable to stored XSS via the plugin's 'su_qrcode' shortcode due to insufficient input sanitization and output escaping
on user supplied attributes.


Authenticated attackers with contributor-level access and above are able to inject arbitrary web scripts in pages that will execute
whenever a user accesses an injected page.


Solution
Update to version 7.0.4 or later.


References

CVE-2024-1808
https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/shortcodes-ultimate/wp-shortcodes-plugin-shortcodes-ultimate-703authenticated-contributor-stored-cross-site-scripting-via-su-qrcode-shortcode
[https://plugins.trac.wordpress.org/changeset/3041647/shortcodes-ultimate](https://plugins.trac.wordpress.org/changeset/3041647/shortcodes-ultimate)



![](/img/anexo-ii---openvas/Anexo-II---OpenVAS.pdf-43-0.png)



[hostedscan.com](https://hostedscan.com/?utm_source=report)



44


Network Vulnerabilities | WordPress Shortcodes Ultimate Plugin &lt; 7.0.5 - Contributor+ Stored XSS Vulnerability Vulnerability Scan Report

#### WordPress Shortcodes Ultimate Plugin &lt; 7.0.5 - Contributor+ Stored XSS Vulnerability



LAST DETECTED

0 days ago



CVSS SCORE

5.5



SEVERITY

Medium



AFFECTED TARGETS

1 target



Description
The WordPress plugin 'Shortcodes Ultimate' is prone to a cross-site scripting (XSS) vulnerability.


The plugin is vulnerable to stored XSS due to not properly escaping some of its shortcodes attributes before they are echoed back to
users.


Attackers with contributor-level permissions can conduct stored XSS attacks.


Solution
Update to version 7.0.5 or later.


References

CVE-2024-2583
[https://wpscan.com/vulnerability/98d8c713-e8cd-4fad-a8fb-7a40db2742a2/](https://wpscan.com/vulnerability/98d8c713-e8cd-4fad-a8fb-7a40db2742a2/)


[hostedscan.com](https://hostedscan.com/?utm_source=report)



![](/img/anexo-ii---openvas/Anexo-II---OpenVAS.pdf-44-0.png)

45


Network Vulnerabilities | WordPress Shortcodes Ultimate Plugin &lt; 7.1.3 - Contributor+ Stored XSS Vulnerability Vulnerability Scan Report

#### WordPress Shortcodes Ultimate Plugin &lt; 7.1.3 - Contributor+ Stored XSS Vulnerability



LAST DETECTED

0 days ago



CVSS SCORE

5.4



SEVERITY

Medium



AFFECTED TARGETS

1 target



Description
The WordPress plugin 'Shortcodes Ultimate' is prone to a cross-site scripting (XSS) vulnerability.


The plugin is vulnerable to stored XSS due to insufficient input sanitization and output escaping on user supplied attributes.


Authenticated attackers with contributor-level access and above are able to inject arbitrary web scripts in pages that will execute
whenever a user accesses an injected page.


Solution
Update to version 7.1.3 or later.


References

CVE-2024-3550
https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/shortcodes-ultimate/wp-shortcodes-plugin-shortcodes-ultimate-712authenticated-contributor-stored-cross-site-scripting-via-shortcode


[hostedscan.com](https://hostedscan.com/?utm_source=report)



![](/img/anexo-ii---openvas/Anexo-II---OpenVAS.pdf-45-0.png)

46


Network Vulnerabilities | ICMP Timestamp Reply Information Disclosure Vulnerability Scan Report

#### ICMP Timestamp Reply Information Disclosure



LAST DETECTED

0 days ago



CVSS SCORE

2.1



SEVERITY

Low



AFFECTED TARGETS

1 target



Description
The remote host responded to an ICMP timestamp request.


The Timestamp Reply is an ICMP message which replies to a Timestamp message. It consists of the originating timestamp sent by the
sender of the Timestamp as well as a receive timestamp and a transmit timestamp.


This information could theoretically be used to exploit weak time-based random number generators in other services.


Solution
Various mitigations are possible:


- Disable the support for ICMP timestamp on the remote host completely


- Protect the remote host by a firewall, and block ICMP packets passing through the firewall in either direction (either completely or only
for untrusted networks)


References

CVE-1999-0524
[https://datatracker.ietf.org/doc/html/rfc792](https://datatracker.ietf.org/doc/html/rfc792)
[https://datatracker.ietf.org/doc/html/rfc2780](https://datatracker.ietf.org/doc/html/rfc2780)



![](/img/anexo-ii---openvas/Anexo-II---OpenVAS.pdf-46-0.png)



[hostedscan.com](https://hostedscan.com/?utm_source=report)



47


Glossary Vulnerability Scan Report

#### Glossary



Accepted Vulnerability


An accepted vulnerability is one which has been manually
reviewed and classified as acceptable to not fix at this
time, such as a false positive scan result or an intentional
part of the system's architecture.


Fully Qualified Domain Name (FQDN)


A fully qualified domain name is a complete domain name
for a specific website or service on the internet. This
includes not only the website or service name, but also the
top-level domain name, such as .com, .org, .net, etc. For
example, 'www.example.com' is an FQDN.


Network Vulnerabilities


The OpenVAS network vulnerability scan tests servers and
internet connected devices for over 150,000
vulnerabilities. OpenVAS uses the Common Vulnerability
Scoring System (CVSS) to quantify the severity of
findings. 0.0 is the lowest severity and 10.0 is the highest.



Vulnerability


A weakness in the computational logic (e.g., code) found
in software and hardware components that, when
exploited, results in a negative impact to confidentiality,
integrity, or availability. Mitigation of the vulnerabilities in
this context typically involves coding changes, but could
also include specification changes or even specification
deprecations (e.g., removal of affected protocols or
functionality in their entirety).


Target


A target represents target is a single URL, IP address, or
fully qualified domain name (FQDN) that was scanned.


Severity


Severity represents the estimated impact potential of a
particular vulnerability. Severity is divided into 5
categories: Critical, High, Medium, Low and Accepted.


CVSS Score


The CVSS 3.0 score is a global standard for evaluating
vulnerabilities with a 0 to 10 scale. CVSS maps to threat
levels:
0.1 - 3.9 = Low
4.0 - 6.9 = Medium
7.0 - 8.9 = High
9.0 - 10.0 = Critical


48


This report was prepared using

##### HostedScan Security ®


For more [information, visit hostedscan.com](https://hostedscan.com/?utm_source=report)


Founded in Seattle, Washington in 2019, HostedScan, LLC. is

dedicated to making continuous vulnerability scanning and risk

management much more easily accessible to more businesses.



HostedScan, LLC.


2212 Queen Anne Ave N
Suite #521
Seattle, WA 98109



[Terms & Policies](https://hostedscan.com/terms-and-policies)
[hello@hostedscan.com](mailto:hello@hostedscan.com)


49



![](/img/anexo-ii---openvas/Anexo-II---OpenVAS.pdf-48-0.png)