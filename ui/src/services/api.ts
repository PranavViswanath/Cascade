import { Paper, CitationCascade, AnalysisResult } from '../types';

const API_BASE_URL = 'http://localhost:8501';

export const api = {
  async extractTextFromPDF(file: File): Promise<string> {
    try {
      const formData = new FormData();
      formData.append('file', file);
      
      const response = await fetch(`${API_BASE_URL}/extract_text`, {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) {
        throw new Error(`Failed to extract text: ${response.status}`);
      }

      const data = await response.json();
      return data.text;
    } catch (error) {
      console.error('Error extracting text from PDF:', error);
      throw error;
    }
  },

  async detectContradictions(claim: string): Promise<Paper[]> {
    try {
      const response = await fetch(`${API_BASE_URL}/detect_contradictions`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ claim }),
      });

      if (!response.ok) {
        throw new Error(`Failed to detect contradictions: ${response.status}`);
      }

      const data = await response.json();
      return data.contradictions || [];
    } catch (error) {
      console.error('Error detecting contradictions:', error);
      throw error;
    }
  },

  async propagateCitations(papers: Paper[]): Promise<CitationCascade> {
    try {
      const response = await fetch(`${API_BASE_URL}/propagate_citations`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ contradictions: papers }),
      });

      if (!response.ok) {
        throw new Error(`Failed to propagate citations: ${response.status}`);
      }

      const data = await response.json();
      return data.citation_cascades || {};
    } catch (error) {
      console.error('Error propagating citations:', error);
      throw error;
    }
  },

  async generateSynthesis(contradictions: Paper[], citations: CitationCascade, claim: string): Promise<string> {
    try {
      const response = await fetch(`${API_BASE_URL}/generate_synthesis`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          contradictions,
          citationCascades: citations,
          claim
        }),
      });

      if (!response.ok) {
        throw new Error(`Failed to generate synthesis: ${response.status}`);
      }

      const data = await response.json();
      return data.synthesis || 'Unable to generate synthesis. Please try again.';
    } catch (error) {
      console.error('Error generating synthesis:', error);
      throw error;
    }
  },

  async analyzeClaim(
    claim: string, 
    setCurrentStep: (step: string) => void,
    onPartialResult: (result: Partial<AnalysisResult>) => void
  ): Promise<AnalysisResult> {
    try {
      // Step 1: Agent 1 - Detect contradictions
      setCurrentStep('analyzing-start');
      await new Promise(resolve => setTimeout(resolve, 500));
      
      setCurrentStep('deep-search');
      const contradictions = await this.detectContradictions(claim);
      
      setCurrentStep('validating-sources');
      await new Promise(resolve => setTimeout(resolve, 800));
      
      // Show partial results after Step 1
      onPartialResult({ claim, contradictions, citationCascades: {}, synthesis: '' });
      
      // Step 2: Agent 2 - Propagate citations
      setCurrentStep('citation-mapping');
      const citations = await this.propagateCitations(contradictions);
      
      setCurrentStep('impact-analysis');
      await new Promise(resolve => setTimeout(resolve, 600));
      
      // Show partial results after Step 2
      onPartialResult({ claim, contradictions, citationCascades: citations, synthesis: '' });
      
      // Step 3: Agent 3 - Generate synthesis
      setCurrentStep('synthesis-prep');
      await new Promise(resolve => setTimeout(resolve, 400));
      
      setCurrentStep('generating-strategy');
      const synthesis = await this.generateSynthesis(contradictions, citations, claim);
      
      return {
        claim,
        contradictions,
        citationCascades: citations,
        synthesis
      };
    } catch (error) {
      console.error('Error analyzing claim:', error);
      throw error;
    }
  }
};