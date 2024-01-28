# Project Overview: CompanyHire.com and Addons.nl

## CompanyHire.com

CompanyHire.com is a centralized platform where companies can register, create, and manage job listings. The goal is to provide a user-friendly interface for companies to connect with potential candidates. Here are the key features:

### Features:

1. **Company Registration:**
   - Companies can register on CompanyHire.com.
   - Business verification through KVK (Chamber of Commerce) number for authenticity.

2. **User Authentication:**
   - Secure login and registration for companies.
   - Password change functionality for account security.

3. **Joblist Management:**
   - Create, update, and delete job listings.
   - Companies have full control over the content of their job listings.

4. **User Search:**
   - Companies can search for users actively looking for jobs.
   - API calls to addons.nl to retrieve user information.

## Addons.nl

Addons.nl represents niche-specific job listing domains like HostpitalJob.nl, SoftwareJob.nl, DeliveryJob.nl, ConsultantJob.nl, etc. These domains will share a common user base and interact with CompanyHire.com through Django Rest API.

### Features:

1. **Shared User Account:**
   - Users have a shared account across all addons.nl domains.
   - Profile creation with CV upload and description to showcase skills and experience.

2. **Django Rest API Integration:**
   - Integration with CompanyHire.com through Django Rest API.
   - API calls to CompanyHire.com for job listings based on domain filters.

3. **Joblist Filtering:**
   - Joblist requests will include a filter based on the domain to retrieve relevant job listings.

## Project Workflow:

### CompanyHire.com Workflow:

- Companies register and manage job listings on CompanyHire.com.
- Business verification ensures the authenticity of registered companies.
- User authentication for secure access.

### Addons.nl Workflow:

- Users register and create profiles on addons.nl domains.
- Shared user account facilitates seamless access across all addons.nl sites.
- Users can upload CVs and provide profile descriptions.

### Interaction between CompanyHire.com and Addons.nl:

- CompanyHire.com provides job listings through Django Rest API.
- Addons.nl sites make API calls to CompanyHire.com to fetch relevant job listings.
- Joblist requests include domain filters to ensure niche-specific content.

## Future Enhancements:

1. **Advanced User Search:**
   - Implement advanced search features for companies on CompanyHire.com to find specific skill sets among users.

2. **Communication Platform:**
   - Integrate a communication platform for companies and users to interact directly.

3. **Notifications and Alerts:**
   - Implement notification systems for users and companies to receive alerts about relevant job listings or potential matches.

This project aims to create a robust and scalable platform connecting companies with potential candidates across various niches, ensuring a smooth user experience and efficient job recruitment processes.