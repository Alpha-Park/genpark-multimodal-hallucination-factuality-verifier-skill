from client import MultimodalHallucinationFactualityVerifierClient

def main():
    client = MultimodalHallucinationFactualityVerifierClient()
    res = client.verify_factuality_consistency('Water freezes at 0 degrees Celsius.', 'Water freezes at 10 degrees.')
    print('Hallucination Verifier: ' + res['verification_id'] + ' (Factuality: ' + str(res['factuality_score']) + ')')
    print('Hallucination Detected: ' + str(res['hallucination_detected']) + ' | Contradictions: ' + str(len(res['contradiction_segments'])))
    print('Audit Report URL: ' + res['hallucination_audit_report_url'])

if __name__ == '__main__':
    main()
