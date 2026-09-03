class MultimodalHallucinationFactualityVerifierClient:
    def verify_factuality_consistency(self, ground_truth_context='The Eiffel Tower is located in Paris, France and was completed in 1889.', agent_generated_statement='The Eiffel Tower in Paris was completed in 1905 during the World Fair.'):
        return {
            'verification_id': 'hal_chk_8812',
            'factuality_score': 0.35,
            'hallucination_detected': True,
            'contradiction_segments': [
                {'claim': 'completed in 1905', 'ground_truth': 'completed in 1889', 'severity': 'CRITICAL_FACTUAL_ERROR'}
            ],
            'calibrated_confidence_score': 0.96,
            'hallucination_audit_report_url': 'https://cleanlab.factuality.genpark.ai/reports/8812.json'
        }
