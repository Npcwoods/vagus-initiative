# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 0.1.x   | :white_check_mark: |

## Reporting a Vulnerability

Please report security vulnerabilities privately:

1. **DO NOT** open a public issue
2. Email: chris@npcwoods.com (or appropriate contact)
3. Allow 48 hours for initial response
4. Allow reasonable time for fix before disclosure

## Security Considerations

### Data Sensitivity

The Vagus Initiative handles potentially sensitive data:

- **Emotional states**: Reveals interaction patterns
- **Trust maps**: Indicates relationship dynamics
- **Session bridges**: Contains topic history
- **Dream summaries**: May expose conversation themes

### Best Practices

#### File Permissions

Set restrictive permissions on data directory:

```bash
chmod 700 $VAGUS_DATA_DIR
chmod 600 $VAGUS_DATA_DIR/*.json
```

#### Encryption at Rest

For sensitive deployments, encrypt state files:

```python
from cryptography.fernet import Fernet

# Encrypt before saving
cipher = Fernet(key)
encrypted = cipher.encrypt(json_data.encode())

# Decrypt after loading
decrypted = cipher.decrypt(encrypted).decode()
data = json.loads(decrypted)
```

#### Secure Backup

- Encrypt backups of state files
- Use secure transfer methods
- Limit backup retention
- Test restore procedures

### What NOT to Store

⚠️ **Never store in Vagus state files:**

- Passwords or credentials
- Financial information
- Medical records (HIPAA-protected)
- Personally identifiable information (PII) of third parties
- Content that could violate privacy laws

### API Keys and Secrets

Keep all secrets out of state:

```python
# BAD - Don't do this
baseline.update({"api_key": "sk-..."})

# GOOD - Use environment
api_key = os.getenv("API_KEY")
```

### Multi-User Considerations

Current version assumes single-user deployment.

For multi-user scenarios:
- Separate data directories per user
- Implement access controls
- Audit logging recommended
- Consider encryption per-user

### Network Security

If exposing state via network:
- Use HTTPS only
- Implement authentication
- Rate limiting recommended
- Input validation essential

## Known Limitations

1. **No built-in encryption**: Files are plaintext JSON
2. **No audit logging**: Changes aren't tracked
3. **No access control**: Anyone with file access can read state
4. **No integrity verification**: Files could be tampered with

## Future Security Enhancements

- [ ] Optional encryption at rest
- [ ] Audit logging
- [ ] Integrity checks
- [ ] Access control hooks
- [ ] Secure multi-user mode

## Compliance Notes

### GDPR (EU)

If serving EU users:
- Implement data deletion capability
- Document data processing
- Obtain consent for emotional tracking
- Provide data export

### CCPA (California)

If serving California users:
- Disclose data collection
- Provide opt-out mechanism
- Honor deletion requests

### HIPAA (Healthcare)

⚠️ **This framework is NOT HIPAA-compliant.**

Do not use with patient data or protected health information (PHI).

## Security Checklist

Before production deployment:

- [ ] Data directory permissions set correctly
- [ ] No secrets in state files
- [ ] Regular backups configured
- [ ] Backup encryption enabled
- [ ] Access logging implemented
- [ ] Incident response plan ready
- [ ] Compliance requirements reviewed

## Questions?

For security questions not covered here:
- Open a private discussion
- Contact maintainers directly

---

*Security is a shared responsibility. Thank you for helping keep users safe.*
