
import React from 'react';
import DocumentUpload from './components/DocumentUpload';
import KnowledgeAssessment from './components/KnowledgeAssessment';
import NovelInformation from './components/NovelInformation';
import KnownInformation from './components/KnownInformation';
import DeepDive from './components/DeepDive';
import TopicTracking from './components/TopicTracking';

function App() {
  return (
    <div className="container mx-auto px-4">
      <h1 className="text-3xl font-bold my-8">RAG Knowledge Tracker</h1>
      <DocumentUpload />
      <KnowledgeAssessment />
      <NovelInformation />
      <KnownInformation />
      <TopicTracking />
    </div>
  );
}

export default App;
