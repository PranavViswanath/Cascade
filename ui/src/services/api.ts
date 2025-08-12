import { Paper, CitationCascade, AnalysisResult } from '../types';

const API_BASE_URL = 'http://localhost:8502';

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
        throw new Error('Failed to extract text from PDF');
      }
      
      const result = await response.json();
      return result.text;
    } catch (error) {
      console.error('Error extracting text from PDF via API:', error);
      // Fallback: try to extract text client-side
      return await this.extractTextClientSide(file);
    }
  },

  async extractTextClientSide(file: File): Promise<string> {
    return new Promise((resolve, reject) => {
      const reader = new FileReader();
      reader.onload = async (e) => {
        try {
          const arrayBuffer = e.target?.result as ArrayBuffer;
          const text = await this.parsePDFText(arrayBuffer);
          resolve(text);
        } catch (error) {
          reject(new Error('Failed to extract text from PDF'));
        }
      };
      reader.onerror = () => reject(new Error('Failed to read PDF file'));
      reader.readAsArrayBuffer(file);
    });
  },

  async parsePDFText(arrayBuffer: ArrayBuffer): Promise<string> {
    try {
      // Import pdf-parse dynamically to avoid SSR issues
      const pdfParse = await import('pdf-parse');
      const data = new Uint8Array(arrayBuffer);
      const result = await pdfParse.default(data);
      return result.text;
    } catch (error) {
      console.error('Error parsing PDF:', error);
      return "PDF text extraction failed. Please try using the text input option instead.";
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
        throw new Error('Failed to detect contradictions');
      }
      
      const result = await response.json();
      return result.contradictions || [];
    } catch (error) {
      console.error('Error detecting contradictions:', error);
      // Return empty array if backend is not available
      return [];
    }
  },

  async propagateCitations(contradictions: Paper[]): Promise<CitationCascade> {
    try {
      const response = await fetch(`${API_BASE_URL}/propagate_citations`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ contradictions }),
      });
      
      if (!response.ok) {
        throw new Error('Failed to propagate citations');
      }
      
      const result = await response.json();
      return result.citation_cascades || {};
    } catch (error) {
      console.error('Error propagating citations:', error);
      // Return empty object if backend is not available
      return {};
    }
  },

  async generateSynthesis(claim: string, contradictions: Paper[], citationCascades: CitationCascade): Promise<string> {
    try {
      const response = await fetch(`${API_BASE_URL}/generate_synthesis`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ claim, contradictions, citationCascades }),
      });
      
      if (!response.ok) {
        throw new Error('Failed to generate synthesis');
      }
      
      const result = await response.json();
      return result.synthesis || 'Unable to generate synthesis. Please try again.';
    } catch (error) {
      console.error('Error generating synthesis:', error);
      // Return a helpful message if backend is not available
      return "Based on this new research, I recommend focusing on exploring the claim through systematic literature review and experimental validation. Consider reaching out to experts in the field for collaboration opportunities. Good luck!";
    }
  },

  async analyzeClaim(claim: string): Promise<AnalysisResult> {
    try {
      console.log('🔍 Frontend: Starting analysis for claim:', claim);
      console.log('🔍 Frontend: API URL:', `${API_BASE_URL}/analyze`);
      
      const response = await fetch(`${API_BASE_URL}/analyze`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ claim }),
      });
      
      console.log('🔍 Frontend: Response status:', response.status);
      console.log('🔍 Frontend: Response ok:', response.ok);
      
      if (!response.ok) {
        const errorText = await response.text();
        console.error('🔍 Frontend: Error response:', errorText);
        throw new Error(`Failed to analyze claim: ${response.status} ${errorText}`);
      }
      
      const result = await response.json();
      console.log('🔍 Frontend: Received result:', result);
      
      return {
        claim: result.claim,
        contradictions: result.contradictions || [],
        citationCascades: result.citation_cascades || {},
        synthesis: result.synthesis || 'Unable to generate synthesis. Please try again.'
      };
    } catch (error) {
      console.error('🔍 Frontend: Error analyzing claim:', error);
      throw new Error(`Failed to analyze claim: ${error.message}`);
    }
  }
};
