import unittest
import python_repos_for_testing as pr
class PythonReposTestCase(unittest.TestCase):
    def setUp(self):
        self.r = pr.get_response()
        self.repo_dicts = pr.get_repo_dicts(self.r)
        self.repo_dict = self.repo_dicts[0]
        self.names,self.plot_dicts = pr.get_names_plot_dicts(self.repo_dicts)
    def test_get_response(self):
        self.assertEqual(self.r.status_code,200)
    def test_repo_dicts(self):
        self.assertEqual(len(self.repo_dicts),30)
        requeied_keys = ['name','owner','stargazers_count','html_url']
        for key in requeied_keys:
            self.assertTrue(key in self.repo_dict.keys())
unittest.main()