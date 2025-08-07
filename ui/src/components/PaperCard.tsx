import React from 'react';
import { motion } from 'framer-motion';
import { FileText, ExternalLink } from 'lucide-react';
import { Paper } from '../types';

interface PaperCardProps {
  paper: Paper;
  index: number;
}

const PaperCard: React.FC<PaperCardProps> = ({ paper, index }) => {
  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ delay: index * 0.1 }}
      className="bg-white rounded-xl shadow-lg border border-gray-100 p-6 card-hover"
    >
      <div className="flex items-start space-x-4">
        <div className="flex-shrink-0">
          <div className="w-12 h-12 bg-gradient-to-br from-primary-500 to-primary-600 rounded-lg flex items-center justify-center">
            <FileText className="w-6 h-6 text-white" />
          </div>
        </div>
        
        <div className="flex-1 min-w-0">
          <motion.h3
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: 0.2 }}
            className="text-lg font-semibold text-gray-900 mb-2 line-clamp-2"
          >
            {paper.title}
          </motion.h3>
          
          <motion.p
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: 0.3 }}
            className="text-gray-600 text-sm leading-relaxed"
          >
            {paper.excerpt}
          </motion.p>
          
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: 0.4 }}
            className="mt-4 flex items-center space-x-2"
          >
            <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-primary-100 text-primary-800">
              Research Paper
            </span>
            <button className="inline-flex items-center text-xs text-primary-600 hover:text-primary-800 transition-colors">
              <ExternalLink className="w-3 h-3 mr-1" />
              View Details
            </button>
          </motion.div>
        </div>
      </div>
    </motion.div>
  );
};

export default PaperCard;
