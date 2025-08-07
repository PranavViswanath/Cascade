import { Paper, CitationCascade, AnalysisResult } from '../types';

const API_BASE_URL = 'http://localhost:8501';

export const api = {
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
      
      return await response.json();
    } catch (error) {
      console.error('Error detecting contradictions:', error);
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
      
      return await response.json();
    } catch (error) {
      console.error('Error propagating citations:', error);
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
      return result.synthesis;
    } catch (error) {
      console.error('Error generating synthesis:', error);
      return 'Unable to generate synthesis at this time. Please try again.';
    }
  },

  async analyzeClaim(claim: string): Promise<AnalysisResult> {
    // For now, we'll simulate the API calls with the Python backend
    // In a real implementation, you'd make actual HTTP requests
    
    // Simulate API delay
    await new Promise(resolve => setTimeout(resolve, 2000));
    
    // Mock data for demonstration
    const contradictions: Paper[] = [
      {
        title: "Limitations of Large Language Models in Reasoning Tasks",
        excerpt: "Recent research suggests that while LLMs excel at pattern recognition, they struggle with complex logical reasoning and abstract thinking tasks."
      },
      {
        title: "The Reasoning Capabilities of Modern AI Systems",
        excerpt: "A comprehensive study reveals that current AI systems, including LLMs, have significant limitations in deductive reasoning and causal inference."
      }
    ];

    const citationCascades: CitationCascade = {
      "Limitations of Large Language Models in Reasoning Tasks": [
        "Cognitive Science Review: AI reasoning limitations",
        "Journal of Artificial Intelligence: Comparative analysis of reasoning capabilities"
      ],
      "The Reasoning Capabilities of Modern AI Systems": [
        "Nature Machine Intelligence: Systematic review of AI reasoning",
        "Science: The future of artificial reasoning"
      ]
    };

    const synthesis = `Based on this new research about LLM reasoning capabilities, I recommend focusing on three key areas for your investigation:

• **Comparative Analysis**: Conduct systematic comparisons between different LLM architectures to identify specific reasoning strengths and weaknesses across various domains.

• **Hybrid Approaches**: Explore combining LLMs with symbolic reasoning systems to enhance logical inference capabilities.

• **Evaluation Framework**: Develop comprehensive benchmarks that test both surface-level pattern matching and deeper causal reasoning abilities.

Good luck with your research!`;

    return {
      claim,
      contradictions,
      citationCascades,
      synthesis
    };
  }
};
