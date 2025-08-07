export interface Paper {
  title: string;
  excerpt: string;
}

export interface CitationCascade {
  [paperTitle: string]: string[];
}

export interface AnalysisResult {
  claim: string;
  contradictions: Paper[];
  citationCascades: CitationCascade;
  synthesis: string;
}

export type InputType = 'text' | 'pdf';

export interface AnalysisStep {
  id: string;
  title: string;
  description: string;
  status: 'pending' | 'running' | 'completed' | 'error';
  result?: any;
}
