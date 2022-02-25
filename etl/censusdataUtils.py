import pandas as pd
import censusdata
from censusdata import censusgeo
from typing import Union, Type


class CensusdataHelper:

    @staticmethod
    def search_census_vars(search_str, year=2019, field='concept', tabletype='detail'):
        df = pd.DataFrame(
            data=censusdata.search('acs5', year, field, search_str, tabletype),
            columns=['id', 'table_name', 'name'])
        df['acs_table_id'] = df.apply(
            lambda r: r['id'].split('_')[0].strip(), axis=1)
        df['name'] = df.apply(lambda r: r['name'].replace(
            '!!', ', ').replace(':,', ':'), axis=1)
        df['table_display_name'] = df.apply(
            lambda r: "{}- {}".format(r['acs_table_id'], r['table_name'].title()), axis=1)
        df = df[['id', 'name', 'table_name',
                 'table_display_name', 'acs_table_id']]
        return df

    def get_voting_pop_vars(year=2019):
        vars = {}
        tables = ['B29001', 'B29002', 'B29003', 'B01003']
        for tbl in tables:
            try:
                tbl = censusdata.censustable(src='acs5', year=year, table=tbl)
                for v in tbl:
                    vars[v] = {"id": v, "year": year} | tbl[v]
            except Exception as e:
                print(f"Missing table: {tbl} - {year}")
        return pd.DataFrame(vars.values())

    @staticmethod
    def censusgeo_bgs(
        county_id: Union[str, list[str]] = '*',
        state: str = '40'
    ) -> Union[Type[censusgeo], list[censusgeo]]:
        """ censusgeo_bgs - gets blockgroup `censusgeo` objects
            - county_id: 
                options:
                - "*" (default): single geo for "all" bgs
                - "<3 digit county FIPS code>": single county FIPS code (w/ out state)
                - "[<3 digit county FIPS code>, ...]: list of 3 digit county FIPS codes
        """
        if not isinstance(county_id, list):
            return censusgeo([('state', state), ('county', county_id), ('block group', '*')])
        else:
            return [censusgeo([('state', state), ('county', c), ('block group', '*')] for c in county_id)]

    @staticmethod
    def censusgeo_counties(state: str = '40'):
        return censusgeo([('state', state), ('county', '*')])

    @staticmethod
    def censusgeo_state(state: str = '40'):
        return censusgeo([('state', state), ('county', '*')])

    @staticmethod
    def get_single_df(geo: Type[censusgeo], year: int, vars: list[str]) -> pd.DataFrame:
        df = censusdata.download('acs5', year, geo, vars)
        data_cols = [c for c in df.columns]
        df['year'] = year

        geo_level = 'county'
        if 'block group' in dict(geo.params()).keys():
            geo_level = 'bg'
        df['geo'] = df.apply(lambda r: dict(r.name.params()), axis=1)
        df['state_id'] = df.apply(lambda r: r['geo']['state'], axis=1)
        if geo_level == 'state':
            df = df[['state_id', 'year'] + data_cols]
        elif geo_level == 'county':
            df['county_id'] = df.apply(lambda r: r['geo']['county'], axis=1)
            df = df[['county_id', 'year'] + data_cols]
        elif geo_level == 'bg':
            df['tract_id'] = df.apply(lambda r: r['geo']['county'], axis=1)
            df['block_group_id'] = df.apply(lambda r: "{}{}{}{}".format(
                r['state_id'], r['county_id'], r['tract_id'], r['geo']['block group']), axis=1)
            df = df[['block_group_id', 'year', 'county_id'] + data_cols]
        return df.reset_index(drop=True)

    @classmethod
    def get_df_by_years(cls, geo, years, vars):
        dfs = [cls.get_single_df(geo, year, vars) for year in years]
        return pd.concat(dfs)

    @classmethod
    def get_df(cls, geos: Union[Type[censusgeo], list[censusgeo]], years: Union[int, list[int]], vars: list[str]) -> pd.DataFrame:
        if not isinstance(geos, list):
            if not isinstance(years, list):
                return cls.get_single_df(geos, years, vars)
            else:
                return cls.get_df_by_years(geos, years, vars)
        else:
            dfs = [cls.get_df_by_years(geo, years, vars) if isinstance(
                years, list) else cls.get_singel_df(geo, years, vars) for geo in geos]
            return pd.concat(dfs)
